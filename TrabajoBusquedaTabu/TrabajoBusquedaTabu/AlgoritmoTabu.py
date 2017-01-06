import numpy
import math
import random

import Vector2D
import TrabajoBusquedaTabu
import Movimiento
import Solucion

class AlgoritmoTabu(object):
    
    def __init__(self,
                 eliteSize = 20, # como mucho 20
                 best_sols = [],
                 tl = [[[0 for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))],
                 th = [],
                 tabuSize = 51113,
                 routerList = [],
                 gridSize = Vector2D.Vector2D(),
                 frequency = [[[0 for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))],
                 tFrequency = [],
                 freqsBest = [[[0 for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))],
                 pxy = 0.0
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
        self.pxy = pxy

    #=====================
    # Funciones auxiliares
    #=====================

    def terminationCondition(self):
        return numIter | cpuTime | solutionLimit | allNeighbourhoodIsTabu | notCostBetter

    def conditionTabuViolated(self):
        pass

    def holdAspirationCriteria(self):
        return a1 or a2

    def a1(s): # s de solucion inicial
        pass

    def a2(s):
        return aMove(s) | aSwapp(s)

    def aMove(s, aspirationValue):
        k =
        aspirationValue = (len(routerList)/2)/2 - math.log2(len(routerList)/2)
        if(tl[i][a][b] + aspirationValue <= k):
            primeS = Movimiento.Movimiento.moveToCell("poner")
        return primeS

    def aSwapp(s, aspirationValue):
        k = 
        if(max(th[]) <= k):
            primeS = Movimiento.Movimiento.swap("poner")
        return primeS

    def fitness(s):
        #return s.giantCompSize+connectedUsers 
        return Solucion.Solucion.getGiantComponentSize(s)+Solucion.Solucion.getConnectedUsers(s)

    def hashId(self):
        res = 0
        for router in self.routerList:
            res = res + hashing[router][TrabajoBusquedaTabu.routersPosition[router]]
        return res

    def hashing(self):
        return random.randint[1, self.tabuSize]

    #==========
    # ALGORITMO
    #==========

    def TabuSearch(self):

        hatSolution = initialSolution
        tl = [[[0 for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))]

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
            if(math.log2(max(gridSize.x, gridSize.y)) == ):
                self.freqsBest = [[[r for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))]
                self.pxy = freqsBest / (freqsBest[[[r for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(routerList))])
            if(math.log2(max(gridSize.x, gridSize.y)) == ):
                #soft
                for r in self.routerList:
                    self.tFrequency.append(r)
                self.tFrequency.sort(reverse = True)
                # cojo los primeros 10% de los routers para cambiarles la posicion acorde a freqsBests
                toChange10 = self.tFrequency[0:len(tFrequency)*0.1]
                self.freqsBest = [[[t for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(toChange10))]
                #strong
                #se cambia el 25% de los routers de posicion
                #la nueva solucion se genera a partir de la actual
                toChange25 = elf.tFrequency[0:len(tFrequency)*0.25]
                self.freqsBest = [[[t for k in range(gridSize.y)] for j in range(gridSize.x)] for i in range(len(toChange25))]
                initialSolution = initialSolution + freqsBest
                hatSolution = initialSolution
        return hatSolution



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


