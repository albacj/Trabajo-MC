import Vector2D
import Solucion 
import numpy
import random

# link de ayuda para el código de las 4 distribuciones:
# http://relopezbriega.github.io/blog/2016/06/29/distribuciones-de-probabilidad-con-python/

class SolutionGenerator:

	def __init__(self, gridSize): #Falta routerPositions y routerRanges
		self.clients = self.assignClients()
		self.gridSize = gridSize 

	def getNumRouters(self, gridSize):
		self.numRouters = self.gridSize / 2
		return numRouters

	def getnumClients (self, numRouters):
		self.numClients = self.numRouters * 3

	def asignClients(self, numClients):

		def rollDice(prob):
			n = random.random()
			return n < prob 
		def calculateProb(x, distributionType):
			for i in range (len(x)):


		clientsPos = []
		currentClientIndex = 0 
		for y in range (self.gridSize.y):
			for x in range (self.gridSize.x):
				prob = 1
				if (rollDice(prob)):
					v = Vector2D.Vector2D(x,y)
					clientPos[currentClientIndex] = v
					currentClientIndex = currentClientIndex + 1


	#Este método ha de asignar acorde a la distribución especificada los routers en el tablero
	
			

	#Este método es el que llamaremos desde la clase TrabajoBusquedaTabu para generar la solucion inicial como adjMatrix
	#def generateSolution_init_(self, clients, routerPositions, routerRanges):
	#	matrixLen = len(routerPositions)+len(clients)
	#	adjMatrix = [[0] * matrixLen for i in range(matrixLen)]

	#	for i in range (0, len(adjMatrix)):
	#		for j in range (0, len(adjMatrix)):
	#			adjMatrix[i][j] = isLinked(i,j)
	#	return adjMatrix		