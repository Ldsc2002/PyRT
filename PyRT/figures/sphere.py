from PyRT.lib.utils import *
from PyRT.components.intersect import *
from PyRT.components.material import *
from PyRT.figures.figure import *

class Sphere(Figure): 
    def __init__(this, center, radius, material) -> None:
        this.center = V3(*center)
        this.radius = radius
        this.material = material

    def intersect(this, orig, dir) -> intersect:
        L = sub(this.center, orig)
        tca = dot(L, dir)
        d2 = dot(L, L) - tca * tca

        if d2 > this.radius * this.radius: return None
        
        thc = (this.radius * this.radius - d2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        
        if t0 < 0: t0 = t1
        if t0 < 0: return None
        
        impact = sumV3(orig, mul(dir, t0))
        normal = norm(sub(impact, this.center))

        return intersect(t0, impact, normal)