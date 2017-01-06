import numpy
import math
import random

import Vector2D
import TrabajoBusquedaTabu

class AlgoritmoTabu(object):
        #=====================
		# Anotaciones de Andreea ^_^ 
		#   Falta un par�metro max_tabu_status que es el m�ximo n�mero de iteraciones que un movimiento puede permanecer en tabu. 
		#	En el caso de que el movimiento no satisfaga ning�n criterio de aspiraci�n para salir de tab�, 
		#   saldr� cuando haya alcanzado max_tabu_status = number_routers / 2. Es importante porque tiene que ir en el algoritmo.
		#   
		#   SUPER IMPORTANTE: Nos falta a�n un m�todo que decida cu�ndo meter las soluciones en tab�, con el que ir rellenando la tl
		#                     Creo que eso viene en el apartado de Neighbourhood definition l�nea 2 y 3, p�gina 9. 
		#   Funciones a�adidas: 
		#		- diversificationCondition, applyIntensification y applyDiversification
	    #           -  Imagino que cuando intensification y diversificationCondition sean true, se aplicar� el applyIntensification y applyDiversification respectivamente
        #=====================
		
    def __init__(self,
                 eliteSize = 20, # como mucho 20
                 best_sols = [],
                 tl = [], 
				 #tl es un array 3D de number_routers x grid_size_x x grid_size_y. TL[router]en[posx][posy].
				 #Referente a tl tambi�n: Por otro lado hay que indicar el �ndice de la �ltima iteraci�n en la que el movimiento se metio en la lista tab�. 
				 #Para poder llevar la cuenta de cu�ntas iteraciones se ha llevado en tab�. Lo necesitamos para el criterio de aspiraci�n, en el que dice que cuando lleve x iteraciones en tab�, se saque =)
                 th = [],  
                 tabuSize = 51113,
                 routerList = [],
                 gridSize = Vector2D.Vector2D(),
                 frequency = [[[0 for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))],
                 tFrequency = [],
                 freqsBest = [[[0 for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))]
                 ):
        self.best_sols = best_sols
        self.eliteSize = eliteSize
        self.tl = tl
        self.th = th
        self.tabuSize = tabuSize
        self.routerList = routerList
        self.gridSize = gridSize
        self.frequency = frequency
        self.tFrequency = tFrequency
        self.freqsBest = freqsBest #freqs_best[r][x][y] indica la frecuencia de colocar el router r en la posicion x,y

    #=====================
    # Funciones auxiliares
    #=====================

    def terminationCondition(self):
        return numIter | cpuTime | solutionLimit | allNeighbourhoodIsTabu | notCostBetter

    def conditionTabuViolated(self):
        pass

    def holdAspirationCriteria(self): 
        pass

    def fitness(s):
        return s.giantCompSize+connectedUsers 
		#Suma el n�mero de conexiones. Cuantas m�s conexiones, mejor fitness. Ambos los queremos maximizar.

    def hashId(self):
        res = 0
        for router in self.routerList:
            res = res + hashing[router][TrabajoBusquedaTabu.routersPosition[router]]
        return res

    def hashing(self):
        return random.randint[1, self.tabuSize]

    def intensificationCondition(self):
        pass	

	def diversificationCondition(self):
		pass

	def applyIntensification(self):
		#trabaja con elite_solutions y freqs_best
		pass

	def applyDiversification(self):
		pass

    #==========
    # ALGORITMO
    #==========

    def TabuSearch(self):

        hatSolution = initialSolution
        tl = []

        while(not terminationCondition):
            primeSolution = Movimiento.Movimiento.applyMovement(self.initialSolution)
            neighbourhood = primeSolution
            for n in neighbourhood:
                if((not conditionTabuViolated) or holdAspirationCriteria):
                    neighbourStar = Movimiento.Movimiento.applyMovement(n)
                if ((not self.tl.contains(n)) and (fitness(n) > fitness(primeSolution))):
                    primeSolution = n
            if(fitness(primeSolution) > fitness(hatSolution)):
                hatSolution = primeSolution
            #update recency and frequency
            self.tl.append(primeSolution)
            self.th.append(initialSolution.hashId() % self.tabuSize)
            for r in self.routerList:
                self.frequency = [[[r for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))]
                self.tFrequency.append(r)
            self.best_sols.append(hatSolution)
            if(intensificacionCondition):
                pass

