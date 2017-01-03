import numpy # librer�a que permite arrays, en este caso, tridimensionales
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
                iterMax = 0,
                eliteSize = 20, # como mucho 20 soluciones, el tamanio max de bestSols
                maxTabuStatus = 0):

		self.gridSize = gridSize
		self.clients = clients
		self.routerPositions = routerPositions
		self.routerRanges = routerRanges
		self.tl = numpy.zeros((routerPositions.len(),gridSize.x,gridSize.y))
		self.tabuSize = tabuSize
		self.th = []
		self.currentIter = 0
		self.iterMax = iterMax
		self.frequency = numpy.zeros((routerPositions.len(),gridSize.x,gridSize.y))
		self.tFrequency = numpy.zeros((routerPositions.len()))
		self.bestSols = numpy.zeros((eliteSize))
		self.eliteSize = eliteSize
		self.maxTabuStatus = maxTabuStatus
		self.initialSolution = initialSolution

	def stopCondition():
		pass

	def isBetterThan(primeSolution, initialSolution):
		res = False
		pass

	def maxIterInTabu():
		pass

	def improvement(primeSolution, hatSolution):
		pass

	def intensifationCondition():
		pass

	def diversificationCondition():
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
			condicionTabuViolada = True # parametro temporal
			criterioAspiracionCumplido = isBetterThan(primeSolution, initialSolution) and maxIterInTabu # los dos criterios de aspiracion
			neighbour = primeSolution
			if((not condicionTabuViolada) or (criterioAspiracionCumplido)): # si se cumple uno de los dos, el estado tabu se cancela
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
			# actualizar frequency
			self.frequency = None
			self.tFrequency = None
			self.bestSols.append(primeSolution)
			# actualizar recency
			th =  None
			tl = None
			if(intensifationCondition):
                # Perform intensification procedure; -> hacer en este nivel
				pass
			if(diversificationCondition):
                # Perform diversification procedures; -> hacer en este nivel
				pass
		return hatSolution