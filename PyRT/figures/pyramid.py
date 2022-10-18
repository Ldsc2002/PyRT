from PyRT.figures.figure import *
from PyRT.figures.triangle import *

class pyramid(figure):
    def __init__(this, vertices, material):
        this.sides = this.generateSides(vertices, material)
        this.material = material

    def generateSides(this, vertices, material):
        if len(vertices) != 4:
            return [None, None, None, None]

        v0, v1, v2, v3 = vertices
        sides = [
            triangle([v0, v3, v2], material),
            triangle([v0, v1, v2], material),
            triangle([v1, v3, v2], material),
            triangle([v0, v1, v3], material),
        ]
        return sides

    def figureIntersect(this, origin, direction):
        t = float("inf")
        intersect = None

        for triangle in this.sides:
            localIntersect = triangle.intersect(origin, direction)
            if localIntersect is not None:
                if localIntersect.distance < t:
                    t = localIntersect.distance
                    intersect = localIntersect

        return intersect