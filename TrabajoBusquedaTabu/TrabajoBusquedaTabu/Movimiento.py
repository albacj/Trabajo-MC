import Solucion

class Movimiento:
	
	def __init__(self, solucion_origen):
		self.solution = solution
		self.routerToMoveToCell = -1
		self.posToMoveToCell = -1 
		self.router1ToSwap = -1
		self.router2ToSwap = -1
	
	def moveToCell(routerToMoveToCell, posToMoveToCell):
		self.routerToMoveToCell = routerToMoveToCell
		self.posToMoveToCell = posToMoveToCell

	def swap(router1ToSwap, router2ToSwap):
		self.router1ToSwap = router1ToSwap 
		self.router2ToSwap = router2ToSwap

	def applyMovement():
		if(self.routerToMoveToCell != -1):
			# el router que estara en una posicion x,y se tiene que mover a otra posicion x,y
			# de la solucion que estoy usando, le cojo la posicion al router y se la cambio a posToMoveToCell
			positions = self.solution.routerPositions
			positions[self.routerToMoveToCell] = self.posToMoveToCell
			newSolution = Solucion.Solucion(self.solution.clients, positions, self.solution.routerRanges)
			return newSolution 
		elif(self.router1ToSwap != -1 and self.router2ToSwap != -1):
			pass
		else:
			print("Some values are set to -1")























		