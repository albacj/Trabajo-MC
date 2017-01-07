
import math
import random

import Vector2D
import Movimiento
import Solucion

class AlgoritmoTabu(object):
	
	def __init__(self,
			sizeGridX,
			sizeGridY,
			routerCount,
			clientCount,
			kFactor,
			startChoice, # 0 = Uniforme, 1= Normal, 2 = Exponencial, 3 = Weibull
			tabuSize=51113, # Tamanio maximo de TH
			eliteSize=20, # como mucho 20,
			):

		self.gridSize = Vector2D.Vector2D(sizeGridX,sizeGridY)
		self.routerCount = routerCount
		self.clientCount = clientCount
		self.maxIteration = sizeGridX * sizeGridY * kFactor
		self.startChoice = startChoice
		self.tabuSize = tabuSize
		self.maxTabuStatus = routerCount / 2
		self.eliteSize = eliteSize
		self.aspirationValue = (self.maxTabuStatus / 2) - math.log2(self.maxTabuStatus)
		self.iterationsPerIntensificationDiversification = math.log2(max(sizeGridX,sizeGridY))

		Solucion.generateHashing(self.tabuSize * 4, self.routerCount, self.gridSize)
		self.resetTabuAlgorithm()

	#=====================
	# Funciones auxiliares
	#=====================

	def resetTabuAlgorithm(self):
		self.tl = [[[0 for k in range(self.gridSize.y)] for j in range(self.gridSize.x)] for i in range(self.routerCount)]
		self.th = [[[0 for k in range(self.gridSize.y)] for j in range(self.gridSize.x)] for i in range(self.routerCount)]
		self.frequency = [[[0 for k in range(self.gridSize.y)] for j in range(self.gridSize.x)] for i in range(self.routerCount)]
		self.tFrequency = [0 for k in range(self.routerCount)]
		self.bestSols = [0 for k in range(self.eliteSize)]
		self.currentIteration = 0

	def setTabu(self, movement : Movimiento.Movimiento):
		movement = Movimiento.Movimiento(movement)
		if movement.isMoveToCell():
			router = movement.routerToMoveToCell
			position = movement.posToMoveToCell
			self.tl[router][position.x][position.y] = self.currentIteration
		else:
			router1 = movement.router1ToSwap
			position1 = movement.solution.routerPositions[router1]
			router2 = movement.router2ToSwap
			position2 = movement.solution.routerPositions[router2]
			self.tl[router1][position1.x][position1.y] = self.currentIteration
			self.tl[router2][position2.x][position2.y] = self.currentIteration

	def aspirationCriteriaSatisfied(self, movement : Movimiento.Movimiento, solution : Solucion.Solucion):
		movement = Movimiento.Movimiento(movement)
		def fitnessImproved():
			originFitness = self.fitness(movement.solution)
			newFitness = self.fitness(solution)
			return newFitness > originFitness

		def enoughIterations():
			if movement.isMoveToCell():
				router = movement.routerToMoveToCell
				position = movement.posToMoveToCell
				return self.tl[router][position.x][position.y] + self.aspirationValue <= self.currentIteration
			else:
				router1 = movement.router1ToSwap
				position1 = movement.solution.routerPositions[router1]
				router2 = movement.router2ToSwap
				position2 = movement.solution.routerPositions[router2]
				tl1 = self.tl[router1][position1.x][position1.y]
				tl2 = self.tl[router2][position2.x][position2.y]
				return (max(tl1, tl2)) + self.aspirationValue <= self.currentIteration

		return fitnessImproved() or enoughIterations()
	
	def fitness(self, solution):
		solution = Solucion.Solucion(solution)
		return ((solution.giantCompSize / solution.routerCount) * 0.5) + ((solution.connectedClients / len(solution.clients)) * 0.5)

	def getAspirationSet(self, movements, solutions):
		#aspiration = []
		#for i in range(len(movements)):
		#	ok = self.aspirationCriteriaSatisfied(movements[i], solutions[i])
		#	if ok:
		#		aspiration
		pass

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

	def getTabuSet(self, movements, solutions):
		tabuSet = []

	def generateTestSolution(self):
		clients = []
		clients.append(Solucion.Client(Vector2D.Vector2D(4.0,4.0)))
		clients.append(Solucion.Client(Vector2D.Vector2D(7.0,7.0)))

		routersPosition = []
		routersPosition.append(Vector2D.Vector2D(0.0,0.0))
		routersPosition.append(Vector2D.Vector2D(0.0,5.0))
		routersPosition.append(Vector2D.Vector2D(7.0,1.0))
		
		routersRange = []
		routersRange.append(2.0)
		routersRange.append(1.0)
		routersRange.append(2.0)

		sol = Solucion.Solucion(clients,routersPosition,routersRange)
		return sol

    def terminationCondition(self, solution, numberOfRouters):
        solution = Solucion.Solucion(solution)
        res = False
        if(solution.getGiantComponentSize.__eq__(numberOfRouters) or self.currentIteration == 100 or len(tl) == 40): # revisar
            res = True
        return res



	#==========
	# ALGORITMO
	#==========

    def TabuSearch(self):
	
		# Generar solucion inicial
        solution = self.generateTestSolution()
        bestSolution = solution
		self.resetTabuAlgorithm()

		while(not terminationCondition(bestSolution, routerCount):

			movements, neighbourhood = self.getNeighbourhood(solution)
			#break
			self.currentIteration = self.currentIteration + 1

				#if((not conditionTabuViolated) or holdAspirationCriteria):
				#	neighbourStar = Movimiento.Movimiento.applyMovement(n)
				#if ((not self.tl.contains(n)) and (fitness(n) > fitness(primeSolution))):
				#	primeSolution = n
			#if(fitness(primeSolution) > fitness(bestSolution)):
			#	bestSolution = primeSolution
			#update recency and frequency
			#self.tl.append(primeSolution)
			#self.th.append(initialSolution.hashId() % self.tabuSize)
			#for r in self.routerList:
			#	self.frequency = [[[r for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))]
			#	self.tFrequency.append(r)
			#self.best_sols.append(bestSolution)
			#if(math.log2(max(gridSize.x, gridSize.y)) == ):
			#	self.freqsBest = [[[r for k in range(gridSize.y)] for j in
			#	range(gridSize.x)] for i in range(len(routerList))]
			#	self.pxy = freqsBest / (freqsBest[[[r for k in range(gridSize.y)] for j in
			#	range(gridSize.x)] for i in range(len(routerList))])
			#if(math.log2(max(gridSize.x, gridSize.y)) == ):
			#	#soft
			#	for r in self.routerList:
			#		self.tFrequency.append(r)
			#	self.tFrequency.sort(reverse = True)
			#	# cojo los primeros 10% de los routers para cambiarles la posicion acorde
			#	a freqsBests
			#	toChange10 = self.tFrequency[0:len(tFrequency)*0.1]
			#	self.freqsBest = [[[t for k in range(gridSize.y)] for j in
			#	range(gridSize.x)] for i in range(len(toChange10))]
			#	#strong
			#	#se cambia el 25% de los routers de posicion
			#	#la nueva solucion se genera a partir de la actual
			#	toChange25 = elf.tFrequency[0:len(tFrequency)*0.25]
			#	self.freqsBest = [[[t for k in range(gridSize.y)] for j in
			#	range(gridSize.x)] for i in range(len(toChange25))]
			#	initialSolution = initialSolution + freqsBest
			#	bestSolution = initialSolution
		return bestSolution
