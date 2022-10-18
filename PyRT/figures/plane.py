from PyRT.figures.figure import *

class plane(figure):
    def __init__(this, center, width, height, material) -> None:
        this.center = V3(*center)
        this.w = width
        this.h = height
        this.material = material

    def figureIntersect(this, orig, direction) -> intersect:
        d = (this.center.y - orig.y) / direction.y
        impact = sumV3(orig, mul(direction, d))
        normal = V3(0, -1, 0)

        if d <= 0 or \
            impact.x > (this.center.x + this.w/2) or impact.x < (this.center.x - this.w/2) or \
            impact.z > (this.center.z + this.h/2) or impact.z < (this.center.z - this.h/2):
            return None

        return intersect(d, impact, normal)