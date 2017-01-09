# Main class

import Vector2D
import Solucion
import SolutionGenerator
import AlgoritmoTabu

gridSize_x = input("Introduzca la anchura del tablero: ")
gridSize_y = input("Introduzca la altura del tablero: ")
factork = input("Introduzca el factor k: ")
probabilityDistribution = input("Introduzca el tipo de Probabilidad. 0 = Uniforme, 1 = Normal, 2 = Exponencial, 3 = Weibull: ")
print("Cargando configuracion seleccionada")
tabuSearch = AlgoritmoTabu.AlgoritmoTabu(int(gridSize_x),int(gridSize_y),float(factork), int(probabilityDistribution))

best = tabuSearch.TabuSearch()
print("\nFin de Busqueda Tabu\n")
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
