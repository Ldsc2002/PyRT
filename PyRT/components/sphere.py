from PyRT.lib.utils import *

class Sphere(object): 
    def __init__(this, center, radius) -> None:
        this.center = center
        this.radius = radius

    def intersect(this, orig, dir) -> bool:
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