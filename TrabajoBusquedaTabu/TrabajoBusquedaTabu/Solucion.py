import Vector2D
import random

class Client: 

	def __init__(self, position : Vector2D.Vector2D):
		self.position = position

hashing = None

def generateHashing(largeHash : int, routerCount : int, gridSize : Vector2D.Vector2D):
	h = [[[random.randint(1, largeHash) for k in range(int(gridSize.y))] for j in range(int(gridSize.x))] for i in range(routerCount)]
	return h

class Solucion:

	def __init__(self, clients, routersPosition, routerRanges):
		self.routerCount = len(routersPosition)
		self.clientCount = len(clients)
		self.clients = clients
		self.routerPositions = routersPosition
		self.routerRanges = routerRanges
		self.adjMatrix = self.generateSolution(clients, routersPosition, routerRanges)
		self.giantComponent = self.getGiantComponent(self.routerCount)
		self.giantCompSize = len(self.giantComponent)
		self.connectedClients = self.getConnectedClients(self.routerCount,self.adjMatrix)
	
	
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

	def getGiantComponent(self, routerCount):
		connectedComponents = self.getConnectedComponents(routerCount, self.adjMatrix)
		return max(connectedComponents, key=len)
			
	# Este método debe calcular los usuarios conectados a routers
	def getConnectedClients(self, routerCount, adjMatrix):
		connectedClients = 0
		# Recorremos las filas de la matriz que corresponda solo a usuarios
		for row in range(routerCount, len(adjMatrix)):
			for col in range(len(adjMatrix[row])):
				if col in self.giantComponent and adjMatrix[row][col] == 1:
					connectedClients = connectedClients + 1
					break
		return connectedClients

	def getConnectedComponents(self, routerCount, adjMatrix):
		result = []
		routers = set(range(routerCount))

		def getNeighborsRouters(routerIndex, routerCount, adjMatrix):
			neighbors = set()
			adjRow = adjMatrix[routerIndex]
			# Recorre todos las posiciones que corresponden a los routers
			for i in range(routerCount):
				value = adjRow[i]
				if value == 1:
					neighbors.add(i)
			return neighbors

		while(len(routers) > 0):
			router = routers.pop()
			connectedComponent = {router}
			pendingRouters = [router]
			while(len(pendingRouters) > 0):
				currentRouter = pendingRouters.pop()
				neighbors = getNeighborsRouters(currentRouter, routerCount, adjMatrix)
				# Eliminamos de neighbors los routers ya visitados
				neighbors.difference_update(connectedComponent)
				# Eliminamos de routers los routers que queden en neighbors
				routers.difference_update(neighbors)
				# Aniadimos los vecinos restantes a la componente conexa
				connectedComponent.update(neighbors)
				# Aniadimos a la lista de routers pendientes los vecinos para visitarlos en las proximas iteraciones
				pendingRouters.extend(neighbors)
			result.append(connectedComponent)
		return result

	def getHash(self):
		hash = 0
		for rIndex in range(self.routerCount):
			position = self.routerPositions[rIndex]
			hash = hash + hashing[rIndex][int(position.x)][int(position.y)]
		return hash