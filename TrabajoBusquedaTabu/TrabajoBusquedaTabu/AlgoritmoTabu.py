import numpy

class AlgoritmoTabu(object):
    
    def __init__(self,
                 eliteSize = 20, # como mucho 20
                 best_sols = numpy.zeros_like(numpy.arange(eliteSize)),
                 tl = [],
                 th =
                 ):
        self.best_sols = best_sols
        self.eliteSize = eliteSize
        self.tl = tl
        self.th = th

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
            th


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


