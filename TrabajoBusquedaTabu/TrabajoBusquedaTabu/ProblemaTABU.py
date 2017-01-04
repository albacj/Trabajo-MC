import numpy # librer�a que permite arrays, en este caso, tridimensionales
import math

import Vector2D
import Movimiento
import Solucion

class ProblemaTABU(object):

	def __init__(self,
				gridSize = Vector2D.Vector2D(),
				clients = [],
                routerPositions = [],
                routerRanges = [],
                initialSolution = None,
                tabuSize = 51113,
                iterMax = math.log2(max(gridSize.x,gridSize.y)),
                eliteSize = 20, # como mucho 20 soluciones, el tamanio max de bestSols
                maxTabuStatus = routerRanges.len()/2,
				aspirationValue = (maxTabuStatus/2)-math.log2(maxTabuStatus)):

		self.gridSize = gridSize
		self.clients = clients
		self.routerPositions = routerPositions
		self.routerRanges = routerRanges
		self.tl = numpy.zeros((routerPositions.len(),gridSize.x,gridSize.y))
		self.tabuSize = tabuSize
		self.th = numpy.zeros((self.tabuSize))
		self.currentIter = 0
		self.iterMax = iterMax
		self.frequency = numpy.zeros((routerPositions.len(),gridSize.x,gridSize.y))
		self.tFrequency = numpy.zeros((routerPositions.len()))
		self.bestSols = numpy.zeros((eliteSize))
		self.eliteSize = eliteSize
		self.maxTabuStatus = maxTabuStatus
		self.initialSolution = initialSolution
		self.aspirationValue = aspirationValue


    # ==================================
    # funciones auxiliares del algoritmo
    # ==================================

	def stopCondition():
		pass

	def isBetterThan(primeSolution, initialSolution):
		res = False
		pass

	def maxIterInTabu():
		return aMoveToCell(s) | aSwapp(s)

	def aMoveToCell(s):
		i = 0
		k = None
		while(i <= k):
			if((tl[i][gridSize.x][gridSize.y] + aspirationValue) <= k):
				primeS = Movimiento.Movimiento.moveToCell(routerPositions[i],p)
		return primeS


	def aSwapp(s):
		i = 0
		k = None
		while(i <= k):
			if((max(th[i][routerPositions[j]],tl[j][routerPositions[i]]) + aspirationValue) <= k):
				primeS = Movimiento.Movimiento.swap(router1ToSwap,router2ToSwap)
		return primeS

	def improvement(primeSolution, hatSolution):
		pass

	def intensifationCondition():
		pass

	def diversificationCondition():
		pass

	def condTabuViolated():
		pass

    #==============================
    # Algoritmo de la B�squeda Tabu
    #==============================

	def TabuSearchAlgorithm(self):

		hatSolution = self.initialSolution
		th = []
		tl = numpy.zeros((self.routerPositions.len(),self.gridSize.x,self.gridSize.y))
		currentIter = 0
		while(not stopCondition):
			primeSolution = Movimiento.Movimiento.applyMovement(self.initialSolution)
			criterioAspiracionCumplido = isBetterThan(primeSolution, initialSolution) and maxIterInTabu # los dos criterios de aspiracion
			neighbour = primeSolution
			if((not condTabuViolated) or (criterioAspiracionCumplido)): # si se cumple uno de los dos, el estado tabu se cancela
				neighbourStar = Movimiento.Movimiento.applyMovement(self.initialSolution)
				if(neighbourStar.issubset(neighbour)): # para asegurar que N* es subconjunto de N
					continue
				else:
					break
			for s in neighbourStar:
				if(): # si s cumple con la función objetivo
					primeSolution = s
			self.initialSolution = primeSolution
			if(improvement(primeSolution, hatSolution)):
				hatSolution = primeSolution
			# frequency
			self.frequency = None
			self.tFrequency = None
			self.bestSols.append(primeSolution)
			# recency
			th =  None
			tl = None
			if(intensifationCondition):
                # actualizar parametros de intensificacion (no queda muy claros cuales son)
				pass
			if(diversificationCondition):
                # actualizar parametros de diversificacion (no queda muy claro cuales son)
				pass
		return hatSolution