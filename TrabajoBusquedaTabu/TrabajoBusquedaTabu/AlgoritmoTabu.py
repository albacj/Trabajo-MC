import math
import random
import copy
import Vector2D
import Movimiento
import Solucion
import SolutionGenerator

class AlgoritmoTabu(object):
	
	def __init__(self,
			sizeGridX,
			sizeGridY,
			kFactor,
			startChoice, # 0 = Uniforme, 1= Normal, 2 = Exponencial, 3 = Weibull
			tabuSize=51113, # Tamanio maximo de TH
			eliteSize=20, # como mucho 20,
			):

		self.gridSize = Vector2D.Vector2D(sizeGridX,sizeGridY)
		self.initialSolution = SolutionGenerator.SolutionGenerator(self.gridSize,startChoice).generateSolution()
		self.routerCount = self.initialSolution.routerCount
		self.clientCount = self.initialSolution.clientCount
		self.maxIteration = sizeGridX * sizeGridY * kFactor
		self.startChoice = startChoice
		self.tabuSize = tabuSize
		self.maxTabuStatus = self.routerCount / 2
		self.eliteSize = eliteSize
		self.aspirationValue = (self.maxTabuStatus / 2) - math.log2(self.maxTabuStatus)
		self.iterationsPerIntensificationDiversification = int(math.log2(max(sizeGridX,sizeGridY)))

		Solucion.hashing = Solucion.generateHashing(self.tabuSize * 4, self.routerCount, self.gridSize)
		self.resetTabuAlgorithm()

	#=====================
	# Funciones auxiliares
	#=====================

	def resetTabuAlgorithm(self):
		self.tl = [[[0 for k in range(self.gridSize.y)] for j in range(self.gridSize.x)] for i in range(self.routerCount)]
		self.th = [False for k in range(self.tabuSize)]
		self.frequency = [[[0 for k in range(self.gridSize.y)] for j in range(self.gridSize.x)] for i in range(self.routerCount)]
		self.tFrequency = [0 for k in range(self.routerCount)]
		self.freqsBest = [[[0 for k in range(self.gridSize.y)] for j in range(self.gridSize.x)] for i in range(self.routerCount)]
		self.bestSols = []
		self.currentIteration = 0

	def setSolutionToBestSols(self, solution):

		def sortBestSol():
			sorted(self.bestSols, key = self.fitness)

		def updateFreqBest(solution):
			for r in range(solution.routerCount):
		#s		solution = Solucion.Solucion(solution)
				routerPosition = solution.routerPositions[r]
				self.freqsBest[r][int(routerPosition.x)][int(routerPosition.y)] = self.freqsBest[r][int(routerPosition.x)][int(routerPosition.y)] + 1

		if(len(self.bestSols) < self.eliteSize):
			self.bestSols.append(solution)
			updateFreqBest(solution)
			sortBestSol()
		else:
			for i in range(len(self.bestSols)):
				best = self.bestSols[i]
				if(self.fitness(best) < self.fitness(solution)):
					self.bestSols[i] = solution
					updateFreqBest(solution)
					break

	def setTabu(self, movement : Movimiento.Movimiento):
		if movement.isMoveToCell():
			router = movement.routerToMoveToCell
			position = movement.posToMoveToCell
			self.tl[router][int(position.x)][int(position.y)] = self.currentIteration
		else:
			router1 = movement.router1ToSwap
			position1 = movement.solution.routerPositions[router1]
			router2 = movement.router2ToSwap
			position2 = movement.solution.routerPositions[router2]
			self.tl[router1][int(position1.x)][int(position1.y)] = self.currentIteration
			self.tl[router2][int(position2.x)][int(position2.y)] = self.currentIteration

	def aspirationCriteriaSatisfied(self, movement : Movimiento.Movimiento, solution : Solucion.Solucion):
		def fitnessImproved():
			originFitness = self.fitness(movement.solution)
			newFitness = self.fitness(solution)
			return newFitness > originFitness

		def enoughIterations():
			if movement.isMoveToCell():
				router = movement.routerToMoveToCell
				position = movement.posToMoveToCell
				return self.tl[router][int(position.x)][int(position.y)] + self.aspirationValue <= self.currentIteration
			else:
				router1 = movement.router1ToSwap
				position1 = movement.solution.routerPositions[router1]
				router2 = movement.router2ToSwap
				position2 = movement.solution.routerPositions[router2]
				tl1 = self.tl[router1][int(position1.x)][int(position1.y)]
				tl2 = self.tl[router2][int(position2.x)][int(position2.y)]
				return (max(tl1, tl2)) + self.aspirationValue <= self.currentIteration

		return fitnessImproved() or enoughIterations()
	
	def fitness(self, solution):
		return ((solution.giantCompSize / solution.routerCount) * 0.5) + ((solution.connectedClients / len(solution.clients)) * 0.5)

	def getNeighbourhood(self, solution):
		movements = []
		neighbourhood = []
		for router in range(self.routerCount):
			originalPosition = solution.routerPositions[router]
			for y in range(self.gridSize.y):
				for x in range(self.gridSize.x ):
					position = Vector2D.Vector2D(float(x),float(y))
					if position == originalPosition:
						continue
					thereIsARouter = False
					routerInThisPlace = None
					for r in range(len(solution.routerPositions)):
						p = solution.routerPositions[r]
						if p == position:
							thereIsARouter = True
							routerInThisPlace = r
							break
					movement = Movimiento.Movimiento(solution)
					if(thereIsARouter):
						movement.swap(router, routerInThisPlace)
					else:
						movement.moveToCell(router, position)
					movements.append(movement)
					neighbourhood.append(movement.applyMovement())
		return movements, neighbourhood

	def getAdmissibleSet(self, movements, solutions):
		admissible = []
		for i in range(len(solutions)):
			s = solutions[i]
			m = movements[i]
			if(not self.isVisited(s)):
				neverHasBeenTabu = False
				if m.isMoveToCell():
					neverHasBeenTabu = self.tl[m.routerToMoveToCell][int(m.posToMoveToCell.x)][int(m.posToMoveToCell.y)] == 0
				else:
					router1 = m.router1ToSwap
					position1 = m.solution.routerPositions[router1]
					router2 = m.router2ToSwap
					position2 = m.solution.routerPositions[router2]
					tl1 = self.tl[router1][int(position1.x)][int(position1.y)]
					tl2 = self.tl[router2][int(position2.x)][int(position2.y)]
					neverHasBeenTabu = tl1 == 0 and tl2 == 0
				if neverHasBeenTabu:
					admissible.append(s)
				elif(self.aspirationCriteriaSatisfied(m,s)):
					admissible.append(s)
						
		return admissible


	def generateTestSolution(self):
		clients = []
		clients.append(Solucion.Client(Vector2D.Vector2D(1.0,3.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(8.0,8.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(3.0,1.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(2.0,2.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(12.0,9.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(11.0,5.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(2.0,12.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(9.0,6.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(5.0,5.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(7.0,11.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(15.0,9.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(7.0,0.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(9.0,15.0))) 
		clients.append(Solucion.Client(Vector2D.Vector2D(9.0,4.0))) 
		clients.append(Solucion.Client(Vector2D.Vector2D(5.0,13.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(13.0,12.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(6.0,9.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(4.0,8.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(10.0,2.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(0.0,12.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(2.0,8.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(10.0,11.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(0.0,6.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(7.0,15.0)))

		routersPosition = []
		routersPosition.append(Vector2D.Vector2D(1.0,5.0))
		routersPosition.append(Vector2D.Vector2D(6.0,7.0))
		routersPosition.append(Vector2D.Vector2D(12.0,8.0))
		routersPosition.append(Vector2D.Vector2D(14.0,3.0))
		routersPosition.append(Vector2D.Vector2D(7.0,13.0))
		routersPosition.append(Vector2D.Vector2D(3.0,6.0))
		routersPosition.append(Vector2D.Vector2D(4.0,11.0))
		routersPosition.append(Vector2D.Vector2D(2.0,15.0))

		routersRange = []
		routersRange.append(2.0)
		routersRange.append(1.0)
		routersRange.append(3.0)
		routersRange.append(2.0)
		routersRange.append(2.0)
		routersRange.append(1.0)
		routersRange.append(3.0)
		routersRange.append(3.0)
		sol = Solucion.Solucion(clients,routersPosition,routersRange)
		return sol

	def terminationCondition(self, solution, numberOfRouters):
		solution = Solucion.Solucion(solution)
		res = False
		if(solution.getGiantComponentSize.__eq__(numberOfRouters) or self.currentIteration == 100 or len(tl) == 40): # revisar
			res = True
		return res

	def isVisited(self, solution):
		hashRes = Solucion.Solucion.getHash(solution)
		return self.th[hashRes % self.tabuSize]

	def setVisited(self, solution, visited = True):
		# pasar la solucion inicial como visitiada
		hashRes = Solucion.Solucion.getHash(solution)
		self.th[hashRes % self.tabuSize] = visited

	def withBestFitness(self,solutions, movements):
		fitnesses = []
		for s in solutions:
			fitnesses.append(self.fitness(s))
		solutionCandidate = None
		movementCandidate = None
		fitnessCandidate = -1
		for i in range(len(solutions)):
			f = fitnesses[i]
			s = solutions[i]
			m = movements[i]
			if(f > fitnessCandidate):
				fitnessCandidate = f
				solutionCandidate = s
				movementCandidate = m
		return solutionCandidate, movementCandidate

	def applyIntensification(self, solution):

		def rollDice(prob):
			n = random.random()
			return n <= prob

		def probXY(r, x, y):
			return self.freqsBest[r][x][y] / N
		
		positions = [None for i in range(self.routerCount)]
		clients = copy.deepcopy(solution.clients)
		routerRanges = copy.deepcopy(solution.routerRanges)
		N = 0
		for r in range(solution.routerCount):
			for y in range(self.gridSize.y):
				for x in range(self.gridSize.x):
					N = N + self.freqsBest[r][x][y]

		for r in range(solution.routerCount):
			placed = False
			while(not placed):
				for y in range(self.gridSize.y):
					for x in range(self.gridSize.x):
						prob = probXY(r,x,y)
						if rollDice(prob):
							positions[r] = Vector2D.Vector2D(x,y)
							placed = True
							break
					if placed:
						break
		return Solucion.Solucion(clients, positions, routerRanges)

	def applySoftDiversification(self, solution):

		def getSortedTFrequency():
			tFreqSorted = copy.deepcopy(self.tFrequency)
			tFreqSorted = sorted(tFreqSorted)
			return tFreqSorted

		def getMostFrequentPosition(router):
			positionCandidate = None
			freqCandidate = -1
			for position in solution.routerPositions:
				freq = self.freqsBest[router][int(position.x)][int(position.y)]
				if freq > freqCandidate:
					freqCandidate = freq
					positionCandidate = position
			return positionCandidate

		tFreqSorted = getSortedTFrequency()
		lasts = len(self.freqsBest) * random.uniform(0.05, 0.1)
		lasts = int(lasts)
		takenLasts = tFreqSorted[:lasts] #cojo los 10% elementos de freqsBest?
		routersToMoveRange = []
		for i in takenLasts:
			routersToMoveRange.append(tFreqSorted.index(i))
		for r in routersToMoveRange:
			solution.routerPositions[r] = getMostFrequentPosition(r)
		return solution

	def applyStrongDiversification(self,solution):

		def getRandomRouter():
			router = None
			while(router == None):
				rndRouter = random.randint(0, self.routerCount - 1)
				if rndRouter not in changedRouters:
					router = rndRouter
			return router

		def getRandomPosition(routerPos):
			position = None
			while(position == None):
				x = random.randint(0, self.gridSize.x - 1)
				y = random.randint(0, self.gridSize.y - 1)
				rndPosition = Vector2D.Vector2D(x,y)
				if rndPosition != routerPos:
					rndPositionDontOverlapAnyRouter = True
					for position in solution.routerPositions:
						if rndPosition == position:
							rndPositionDontOverlapAnyRouter = False
							break
					if rndPositionDontOverlapAnyRouter:
						position = rndPosition
			return position

		changedRouters = []
		numRoutersToChange = int(self.routerCount * 0.25)
		for i in range(numRoutersToChange):
			router = getRandomRouter()
			newPosition = getRandomPosition(solution.routerPositions[router])
			solution.routerPositions[router] = newPosition

		return solution


	#==========
	# ALGORITMO
	#==========

	def TabuSearch(self):
	
		# Generar solucion inicial
		currentSolution = self.initialSolution #s'
		bestSolution = currentSolution #s gorrito
		self.resetTabuAlgorithm()
		self.setVisited(bestSolution)
		maxPenaltyValue = 3
		currentPenaltyValue = 0
		previousBestSolutionFitness = self.fitness(bestSolution)
		
		while(self.currentIteration < self.maxIteration):
			print("Iteracion actual: " + str(self.currentIteration))
			movements, neighbourhood = self.getNeighbourhood(currentSolution)
			admissibleSet = self.getAdmissibleSet(movements, neighbourhood)
			bestLocal, bestMovement = self.withBestFitness(admissibleSet, movements)
			currentSolution = bestLocal
			
			if(self.fitness(currentSolution) > self.fitness(bestSolution)):
				bestSolution = currentSolution
				previousBestSolutionFitness = self.fitness(bestSolution)
			else:
				currentPenaltyValue = currentPenaltyValue + 1

			print("Hash: " + str(bestLocal.getHash()))
			print("Fitness de la iteracion: " + str(self.fitness(bestLocal)))
			print("Fitness de la mejor solucion: " + str(previousBestSolutionFitness))

			##update recency and frequency
			self.setTabu(bestMovement)
			self.setVisited(bestLocal) # hacer la solucion visitada
			
			if bestMovement.isMoveToCell():
				router = bestMovement.routerToMoveToCell
				position = bestMovement.posToMoveToCell
				self.frequency[router][int(position.x)][int(position.y)] = self.frequency[router][int(position.x)][int(position.y)] + 1
				self.tFrequency[router] = self.tFrequency[router] + 1
			else:
				router1 = bestMovement.router1ToSwap
				position1 = bestMovement.solution.routerPositions[router1]
				router2 = bestMovement.router2ToSwap
				position2 = bestMovement.solution.routerPositions[router2]
				self.frequency[router1][int(position1.x)][int(position1.y)] = self.frequency[router1][int(position1.x)][int(position1.y)] + 1
				self.frequency[router2][int(position2.x)][int(position2.y)] = self.frequency[router2][int(position2.x)][int(position2.y)] + 1
				self.tFrequency[router1] = self.tFrequency[router1] + 1
				self.tFrequency[router2] = self.tFrequency[router2] + 1

			self.setSolutionToBestSols(bestLocal)

			if currentPenaltyValue >= maxPenaltyValue:
				print("Aplicando intensificacion y diversificacion a la solucion")
				for i in range(self.iterationsPerIntensificationDiversification):
					#intensification
					currentSolution = self.applyIntensification(currentSolution)
					#diversification
					currentSolution = self.applySoftDiversification(currentSolution)
					currentSolution = self.applyStrongDiversification(currentSolution)
				currentPenaltyValue = 0

			self.currentIteration = self.currentIteration + 1
			if self.fitness(bestSolution) == 1.0:
				break

		return bestSolution
		print (bestSolution)
