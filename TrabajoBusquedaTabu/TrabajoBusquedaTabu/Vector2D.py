import math

class Vector2D(object):

	def __init__(self, x : float, y : float):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __repr__(self):
		return "(" + self.x + "," + self.y + ")"

	def __eq__(self, other):
		res = False
		if isinstance(other, Vector2D):
			res = self.x == other.x and self.y == other.y
		return res


def getEuclideanDistance(v0, v1):
	x2 = (v1.x - v0.x)**2
	y2 = (v1.y - v0.y)**2
	return math.sqrt(x2 + y2)

