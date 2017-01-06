import Solucion
import copy

class Movimiento:
	
	def __init__(self, solution):
		self.solution = solution
		self.routerToMoveToCell = -1
		self.posToMoveToCell = -1 
		self.router1ToSwap = -1
		self.router2ToSwap = -1

	def isMoveToCell(self):
		return self.routerToMoveToCell is not -1
	
	def moveToCell(self, routerToMoveToCell, posToMoveToCell):
		self.routerToMoveToCell = routerToMoveToCell
		self.posToMoveToCell = posToMoveToCell

	def swap(self, router1ToSwap, router2ToSwap):
		self.router1ToSwap = router1ToSwap 
		self.router2ToSwap = router2ToSwap

	def applyMovement(self):
		if(self.routerToMoveToCell != -1):
			positions = copy.deepcopy(self.solution.routerPositions)
			clients = copy.deepcopy(self.solution.clients)
			routerRanges = copy.deepcopy(self.solution.routerRanges)
			positions[self.routerToMoveToCell] = self.posToMoveToCell
			newSolution = Solucion.Solucion(clients, positions, routerRanges)
			return newSolution 
		elif(self.router1ToSwap != -1 and self.router2ToSwap != -1):
			positions = copy.deepcopy(self.solution.routerPositions)
			clients = copy.deepcopy(self.solution.clients)
			routerRanges = copy.deepcopy(self.solution.routerRanges)
			positionAux = positions[self.router1ToSwap]
			positions[self.router1ToSwap] = positions[self.router2ToSwap]
			positions[self.router2ToSwap] = positionAux
			newSolution = Solucion.Solucion(clients, positions, routerRanges)
			return newSolution
		else:
			print("ERROR. Some values are set to -1")























		