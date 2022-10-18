from PyRT.figures.figure import *

class triangle(figure):
    def __init__(this, vertices, material):
        newVertices = [V3(*v) for v in vertices]

        this.vertices = newVertices
        this.material = material

    def figureIntersect(this, origin, direction):
        v0, v1, v2 = this.vertices
        normal = cross(sub(v1, v0), sub(v2, v0))
        determinant = dot(normal, direction)

        if abs(determinant) < 0.0001:
            return None

        distance = dot(normal, v0)
        t = (dot(normal, origin) + distance) / determinant
        if t < 0:
            return None

        point = sumV3(origin, mul(direction, t))
        u, v, w = barycentric(v0, v1, v2, point)

        if w < 0 or v < 0 or u < 0:
            return None
        
        return intersect(distance, point, norm(normal))