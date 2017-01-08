import Vector2D
import Solucion 

# link de ayuda para el código de las 4 distribuciones:
# http://relopezbriega.github.io/blog/2016/06/29/distribuciones-de-probabilidad-con-python/

class SolutionGenerator:

	def __init__(self, clients): #Falta routerPositions y routerRanges
		self.clients = self.AssignClients()
		
		self.gridSize = Vector2D.Vector2D(sizeGridX,sizeGridY)

	def getNumRouters(self, gridSize):
		self.numRouters = self.gridSize / 2
		return numRouters

	def getnumClients (self, numRouters):
		self.numClients = self.numRouters * 3

	def AssignClients(self, numClients):
		clients = [] 
		for i in range (1, self.numClients):
			a = int(random.uniform(0,grid_size-1))
			b = int(random.uniform(0,grid_size-1))
			clients.append((a,b))
		return clients
		
	#Este método ha de asignar acorde a la distribución especificada los routers en el tablero
	def AssignRoutersPositions(self, gridSize, distribution_probability):
		routerPositions = []
		for i in range (1, self.numRouters):

			

	#Este método es el que llamaremos desde la clase TrabajoBusquedaTabu para generar la solucion inicial como adjMatrix
	#def generateSolution_init_(self, clients, routerPositions, routerRanges):
	#	matrixLen = len(routerPositions)+len(clients)
	#	adjMatrix = [[0] * matrixLen for i in range(matrixLen)]

	#	for i in range (0, len(adjMatrix)):
	#		for j in range (0, len(adjMatrix)):
	#			adjMatrix[i][j] = isLinked(i,j)
	#	return adjMatrix		