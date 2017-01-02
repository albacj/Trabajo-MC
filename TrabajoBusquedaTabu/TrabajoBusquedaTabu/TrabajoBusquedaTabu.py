#Clase main. 
import Vector2D

#v0 = Vector2D.Vector2D(0.0,3.0)
#v1 = Vector2D.Vector2D(4.0,1.0)

#print(Vector2D.getEuclideanDistance(v0, v1))

import Solucion

clients = []
clients.append(Solucion.Client(Vector2D.Vector2D(7.0,7.0)))
clients.append(Solucion.Client(Vector2D.Vector2D(2.0,4.0)))
routersPosition = []
routersPosition.append(Vector2D.Vector2D(0.0,0.0))
routersPosition.append(Vector2D.Vector2D(7.0,0.0))
routersRange = []
routersRange.append(1.0)
routersRange.append(1.0)
sol = Solucion.Solucion(clients,routersPosition,routersRange)
for col in sol.adjMatrix:
	print(col)