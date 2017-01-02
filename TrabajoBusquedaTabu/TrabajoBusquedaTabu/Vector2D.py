import math

class Vector2D(object):

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y


def getEuclideanDistance(v0, v1):
    x2 = (v1.x - v0.x)**2
    y2 = (v1.y - v0.y)**2
    return math.sqrt(x2 + y2)