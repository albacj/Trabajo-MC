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

tabuSearch = AlgoritmoTabu.AlgoritmoTabu(4,4,1,4)

best = tabuSearch.TabuSearch()
print("Fin de Busqueda Tabu")
print("Matriz de adyacencia")
for row in best.adjMatrix:
	print(row)
print("Tamaño componente gigante")
print(best.giantCompSize)
print("Numero de clientes conectados a componente gigante")
print(best.connectedClients)
print("Posicion de routers")
for pos in best.routerPositions:
	print(pos)
print("Posicion de clientes")
for c in best.clients:
	print(c.position)
print("Rango de routers")
print(best.routerRanges)