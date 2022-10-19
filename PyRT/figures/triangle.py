from PyRT.figures.figure import *

class triangle(figure):
    def __init__(this, vertices, material):
        this.vertices = [V3(*v) for v in vertices]
        this.material = material

    def figureIntersect(this, orig, direction) -> intersect:
        v0, v1, v2 = this.vertices

        edge1 = sub(v1, v0)
        edge2 = sub(v2, v0)

        h = cross(direction, edge2)
        a = dot(edge1, h)

        if a > -1e-6 and a < 1e-6:
            return None
        
        f = 1 / a
        s = sub(orig, v0)
        u = f * dot(s, h)

        if u < 0 or u > 1:
            return None

        q = cross(s, edge1)
        v = f * dot(direction, q)

        if v < 0 or u + v > 1:
            return None

        t = f * dot(edge2, q)

        if t > 1e-6:
            impact = sumV3(orig, mul(direction, t))
            normal = norm(cross(edge1, edge2))

            return intersect(t, impact, normal)
        
        return None