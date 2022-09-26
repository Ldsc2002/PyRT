from PyRT.lib.utils import *

class Sphere(object): 
    def __init__(this, center, radius, color = color(255, 255, 255)) -> None:
        this.center = center
        this.radius = radius
        this.color = color

    def getColor(this) -> color:
        return this.color

    def intersect(this, orig, dir) -> color:
        L = sub(this.center, orig)
        tca = dot(L, dir)
        d2 = dot(L, L) - tca * tca
        if d2 > this.radius * this.radius: return False
        thc = (this.radius * this.radius - d2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0: t0 = t1
        if t0 < 0: return False
        return True