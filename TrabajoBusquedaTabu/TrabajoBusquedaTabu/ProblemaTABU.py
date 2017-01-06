import numpy # librer�a que permite arrays, en este caso, tridimensionales
import Vector2D
import Movimiento

class ProblemaTABU(object):

    def __init__(self,
                 gridSize = Vector2D.Vector2D(),
                 clients = [],
                 routerPositions = [],
                 routerRanges = [],
                 initialSolution = None,
                 tabuSize = 0,
                 iterMax = 0,
                 eliteSize = 0, 
                 maxTabuStatus = 0,
                 recency = 0):

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
        self.bestSols = numpy.zeros((20)) # como mucho 20
        self.eliteSize = eliteSize
        self.maxTabuStatus = maxTabuStatus
        self.initialSolution = initialSolution

    def isBetterThan(primeSolution, initialSolution):
        res = False # tiene que devolver True al final
    
    def maxIterInTabu():
        pass
    
    #==============================
    # Algoritmo de la B�squeda Tabu
    #==============================
    
    def TabuSearchAlgorithm(self):
    
        hatSolution = self.initialSolution
        th = []
        tl = numpy.zeros((self.routerPositions.len(),self.gridSize.x,self.gridSize.y))
        currentIter = 0
        stopCondition = False # parametro temporal
        while(not stopCondition):
            condicionTabuViolada = True # parametro temporal
            criterioAspiracionCumplido = bestFitness and maxIterInTabu # los dos criterios de aspiracion
            if((not condicionTabuViolada) or (criterioAspiracionCumplido)):
                #genera subconjunto de soluciones N*(s) -> hacer en este nivel
                pass
            #elijo el mejor conjunto de soluci�n s' (primeSolution) perteneciente a N*(s) que cumpla la f. objetivo
            # -> hacer en este nivel
            self.initialSolution = primeSolution
            improvement = True # parametro temporal
            if(improvement): # "improvement(primeSolution, hatSolution)" 
                hatSolution = primeSolution
            frequency = None #(,,) actualizar
            recency = None # actualizar
            intensificationCondition = True # parametro temporal
            if(intensifationCondition):
                # Perform intensification procedure; -> hacer en este nivel
                pass
            diversificationCondition = True # parametro temporal
            if(diversificationCondition):
                # Perform diversification procedures; -> hacer en este nivel
                pass
        return hatSolution
    