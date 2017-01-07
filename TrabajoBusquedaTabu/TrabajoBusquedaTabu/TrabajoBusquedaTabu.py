# Main class
#import Vector2D
#import Solucion
#import SolutionGenerator
import AlgoritmoTabu


#for row in sol.adjMatrix:
#	print(row)
#ccs = sol.getConnectedComponents(len(routersPosition), sol.adjMatrix)
#print(ccs)
#giant = sol.giantCompSize
#users = sol.connectedUsers
#print(giant, users)

tabuSearch = AlgoritmoTabu.AlgoritmoTabu(8,8,4,12,1,0)
best = tabuSearch.TabuSearch()
print(best)
