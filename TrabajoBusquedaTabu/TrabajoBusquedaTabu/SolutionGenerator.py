import Vector2D
import Solucion 
import numpy as np
import random
import math

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

		def uniform(a, b):
			return 1 / (b - a)

		def gaussian(x, mu, sig):
			return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

		def exponential(a, x):
			return a * math.e**(-a*x)

		def weibull(l,k,x):
			return (k/l) * ((x/l)**k-1) * (math.e**(-(x/l)**k))

		def getUniformProbability():
			xSet = np.linspace(0,elementSize,elementSize)
			s = uniform(0, elementSize)
			return s

		def getNormalProbability():
			xSet = np.linspace(-4,7,elementSize)
			s = gaussian(xSet[x], 2, 3)
			return s

		def getExponentialProbability():
			xSet = np.linspace(0.0,3.0,elementSize)
			s = exponential(1.0, xSet[x])
			return s

		def getWeibullProbability():
			xSet = np.linspace(0.5,2.0,elementSize)
			s = weibull(1.0, 5.0, xSet[x])
			return max(s, 0.05)

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