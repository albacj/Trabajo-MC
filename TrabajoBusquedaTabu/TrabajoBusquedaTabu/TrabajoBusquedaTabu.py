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

tabuSearch = AlgoritmoTabu.AlgoritmoTabu(8,8,3,2,4,0)
tabuSearch.TabuSearch()
