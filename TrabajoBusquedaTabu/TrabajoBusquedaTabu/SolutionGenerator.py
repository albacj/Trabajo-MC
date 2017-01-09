import Vector2D
import Solucion 
import numpy as np
import random


class SolutionGenerator:

	def __init__(self, gridSize, generationType): #Falta routerPositions y routerRanges
		self.gridSize = gridSize
		self.generationType = generationType  # 0 = Uniforme, 1 = Normal, 2 = Exponencial, 3 = Weibull

	def getNumRouters(self):
		numRouters = self.gridSize.x * 0.5
		return int(numRouters)

	def getnumClients (self):
		numClients = self.getNumRouters() * 3
		return int(numClients)

	def getProbability(self, x, elementSize):

		def getUniformProbability():
			s = np.random.uniform(0.1,1.0,elementSize)
			return max(s[x],0.01)

		def getNormalProbability():
			s = np.random.normal(0, 0.1, elementSize) # mu = 0, sigma = 0.1
			return max(s[x],0.01)

		def getExponentialProbability():
			s = np.random.exponential(1.0, elementSize)
			return max(s[x],0.01)

		def getWeibullProbability():
			s = np.random.weibull(4.0, elementSize) # a = 4
			return max(s[x],0.01)

		if self.generationType == 0:
			return getUniformProbability()
		elif self.generationType == 1:
			return getNormalProbability()
		elif self.generationType == 2:
			return getExponentialProbability()
		else:
		    return getWeibullProbability()

	def assignClients(self):

		def rollDice(prob):
			n = random.random()
			return n < prob

		clientSize = self.getnumClients()
		clientPositions = [None for i in range(clientSize)]
		pendingClients = clientSize
		currentClient = 0
		prob = self.getProbability(currentClient, clientSize)
		while(pendingClients > 0):
			for y in range(int(self.gridSize.y)):
				for x in range (int(self.gridSize.x)):
					client = Solucion.Client(Vector2D.Vector2D(x,y))
					if client not in clientPositions:
						if (rollDice(prob)):
							clientPositions[currentClient] = client
							currentClient = currentClient + 1
							pendingClients = pendingClients - 1
							if pendingClients == 0:
								return clientPositions
							else:
								prob = self.getProbability(currentClient, clientSize)

		return clientPositions

	def assignRouters(self):

		def rollDice(prob):
			n = random.random()
			return n < prob

		routerSize = self.getNumRouters()
		routerPositions = [None for i in range(routerSize)]
		pendingRouters = routerSize
		currentRouter = 0
		prob = self.getProbability(currentRouter, routerSize)
		while(pendingRouters > 0):
			for y in range(int(self.gridSize.y)):
				for x in range (int(self.gridSize.x)):
					pos = Vector2D.Vector2D(x,y)
					if pos not in routerPositions:
						if (rollDice(prob)):
							routerPositions[currentRouter] = pos
							currentRouter = currentRouter + 1
							pendingRouters = pendingRouters - 1
							if pendingRouters == 0:
								return routerPositions
							else:
								prob = self.getProbability(currentRouter, routerSize)

		return routerPositions

	def assignRouterRanges(self):
		routerRanges = [random.randint(1, 3) for i in range(self.getNumRouters())]
		return routerRanges		

	def generateSolution(self):
		clients = self.assignClients()
		routerPos = self.assignRouters()		
		routerRanges = self.assignRouterRanges()
		return Solucion.Solucion(clients, routerPos, routerRanges)