import Vector2D
import Solucion 

# link de ayuda para el código de las 4 distribuciones:
# http://relopezbriega.github.io/blog/2016/06/29/distribuciones-de-probabilidad-con-python/

class SolutionGenerator:

	def __init__(self, clients): #Falta routerPositions y routerRanges
		self.clients = self.AssignClients()

	#Este método ha de asignar aleatoriamente a los clientes en el tablero
	def AssignClients(self):
		clients = [] 
		grid_size = 32 #Vector2D.Vector2D(15.0,15.0)
		numberOfRouters = grid_size / 2
		numberOfClients = numberOfRouters * 3
		for i in range (1, numberOfClients):
			a = int(random.uniform(0,grid_size-1))
			b = int(random.uniform(0,grid_size-1))
			clients.append((a,b))
		return clients
		
	#Este método ha de asignar acorde a la distribución especificada los routers en el tablero
	#def AssignRoutersPositions(self, distribution_probability):
		#routerPositions = []
		#grid_size = 32 #Vector2D.Vector2D(15.0,15.0)
		#numberOfRouters = grid_size / 2
		#for i in range (1, numberOfRouters):
			

	#Este método es el que llamaremos desde la clase TrabajoBusquedaTabu para generar la solucion inicial como adjMatrix
	#def generateSolution_init_(self, clients, routerPositions, routerRanges):
	#	matrixLen = len(routerPositions)+len(clients)
	#	adjMatrix = [[0] * matrixLen for i in range(matrixLen)]

	#	for i in range (0, len(adjMatrix)):
	#		for j in range (0, len(adjMatrix)):
	#			adjMatrix[i][j] = isLinked(i,j)
	#	return adjMatrix		