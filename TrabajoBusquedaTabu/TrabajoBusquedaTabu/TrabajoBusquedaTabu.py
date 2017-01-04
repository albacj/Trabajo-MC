# Main class
import Vector2D
import Solucion
import SolutionGenerator 
#v0 = Vector2D.Vector2D(0.0,3.0)
#v1 = Vector2D.Vector2D(4.0,1.0)

#clients = []
#clients.append(SolutionGenerator.SolutionGenerator.AssignClients)

clients = []
clients.append(Solucion.Client(Vector2D.Vector2D(3.0,5.0)))

routersPosition = []
routersPosition.append(Vector2D.Vector2D(4.0,5.0))
routersPosition.append(Vector2D.Vector2D(6.0,5.0))

routersRange = []
routersRange.append(1.0)
routersRange.append(1.9)
sol = Solucion.Solucion(clients,routersPosition,routersRange)
for col in sol.adjMatrix:
	print(col)