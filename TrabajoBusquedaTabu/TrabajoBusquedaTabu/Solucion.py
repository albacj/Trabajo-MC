import Vector2D

class Client: 

	def __init__(self, position : Vector2D.Vector2D):
		self.position = position

class Solucion:

	def __init__(self, clients, routersPosition, routersRange):
		self.adjMatrix = self.generateSolution(clients, routersPosition, routersRange)
		self.giantCompSize = 0
		self.connectedUsers = 0
		
	# Falta: actualizar giantCompSize y connectedUsers
	# giantCompSize Hay que averiguar todas las componentes conexas de los routers en la matriz de adyacencia (viendolo como grafo) para ver cual es la mas grande
	# connectedUsers Hay que mirar la matriz de adyacencia y ver todos los usuarios conectados a un router

	def generateSolution(self, clients, routerPositions, routerRanges):

		def isLinked(n0, n1):
			if n0 == n1:
				return 0
			n0IsRouter = n0 <= len(routerPositions) - 1
			n1IsRouter = n1 <= len(routerPositions) - 1
			if(not n0IsRouter and not n1IsRouter):
				return 0
			p0 = None
			p1 = None
			r0 = 0
			r1 = 0
			if n0IsRouter:
				p0 = routerPositions[n0]
				r0 = routerRanges[n0]
			else:
				p0 = clients[n0-len(routerPositions)].position
			if n1IsRouter:
				p1 = routerPositions[n1]
				r1 = routerRanges[n1]
			else:
				p1 = clients[n1-len(routerPositions)].position

			if(r0 + r1 >= Vector2D.getEuclideanDistance(p0,p1)):
				return 1
			else:
				return 0

		matrixLen = len(routerPositions)+len(clients)
				
		
		adjMatrix = [[0] * matrixLen for i in range(matrixLen)]

		for i in range (0, len(adjMatrix)):
			for j in range (0, len(adjMatrix)):
				adjMatrix[i][j] = isLinked(i,j)
		return adjMatrix	

# Este método debe calcular los usuarios conectados a routers
#	def calculateConnectedUsers(self, adjMatrix):
#		for i in range (0, len(adjMatrix)-1):
#			if (not routerPositions in adjMatrix[i]): 
#				if (clients in adjMatrix[i]):
#					connectedUsers = connectedUsers + 1
#		return connectedUsers