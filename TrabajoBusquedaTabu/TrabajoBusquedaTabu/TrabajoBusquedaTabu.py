# Main class
#import Vector2D
#import Solucion
#import SolutionGenerator
import AlgoritmoTabu
import numpy as np

a = 2
w = np.random.weibull(a, 16)
#print (w)


print ("Matematicas para la Computacion >> Curso 2016/2017")
print ("")
print ("Algoritmo Tabu aplicado a problema de emplazamiento de nodos")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Alumnas: Alba Carmona Jamardo y Andreea Oprescu")
print("Docente: Maria Isabel Hartillo Hermoso")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Por favor, introduzca los siguientes parametros para ejecutar el algoritmo")
print("")
gridSize = input("Tamano del tablero:")
distributionType = input("Tipo de distribucion: ")
#for row in sol.adjMatrix:
#	print(row)
#ccs = sol.getConnectedComponents(len(routersPosition), sol.adjMatrix)
#print(ccs)
#giant = sol.giantCompSize
#users = sol.connectedUsers
#print(giant, users)

#tabuSearch = AlgoritmoTabu.AlgoritmoTabu(8,8,4,12,1,0)
#best = tabuSearch.TabuSearch()
#print(best)

