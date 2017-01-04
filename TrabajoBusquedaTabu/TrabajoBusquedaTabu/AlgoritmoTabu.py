import numpy
import math
import random

import Vector2D
import TrabajoBusquedaTabu

class AlgoritmoTabu(object):
    
    def __init__(self,
                 eliteSize = 20, # como mucho 20
                 best_sols = [],
                 tl = [],
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
        self.freqsBest = freqsBest

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
        pass

    def hashId(self):
        res = 0
        for router in self.routerList:
            res = res + hashing[router][TrabajoBusquedaTabu.routersPosition[router]]
        return res

    def hashing(self):
        return random.randint[1, self.tabuSize]

    def intensificationCondition(self):
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



#sBest ← s0
#tabuList ← []
#while (not stoppingCondition())
#	candidateList ← []
#	bestCandidate ← null
#	for (sCandidate in sNeighborhood)
#		if ( (not tabuList.contains(sCandidate)) and (fitness(sCandidate) > fitness(bestCandidate)) )
#			bestCandidate ← sCandidate
#		end
#	end
#	if (fitness(bestCandidate) > fitness(sBest)) # improvement del documento
#		sBest ← bestCandidate
#	end
#	tabuList.push(bestCandidate);
#	if (tabuList.size > maxTabuSize)
#		tabuList.removeFirst()
#	end
#end
#return sBest


