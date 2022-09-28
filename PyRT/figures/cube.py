from PyRT.lib.utils import *
from PyRT.components.intersect import *
from PyRT.components.material import *
from PyRT.figures.figure import *

class cube(figure): 
    def __init__(this, center, side, material) -> None:
        this.center = V3(*center)
        this.side = side
        this.material = material

    def intersect(this, orig, direction) -> intersect:
        tmin = float('-inf')
        tmax = float('inf')

        for i in range(3):
            if abs(direction[i]) < 1e-6:
                if orig[i] < this.center[i] - this.side / 2 or orig[i] > this.center[i] + this.side / 2:
                    return None
            else:
                t1 = (this.center[i] - this.side / 2 - orig[i]) / direction[i]
                t2 = (this.center[i] + this.side / 2 - orig[i]) / direction[i]

                if t1 > t2:
                    t1, t2 = t2, t1

                if t1 > tmin:
                    tmin = t1

                if t2 < tmax:
                    tmax = t2

                if tmin > tmax:
                    return None

        if tmin < 0:
            tmin = tmax

            if tmin < 0:
                return None

        impact = sumV3(orig, mul(direction, tmin))
        normal = norm(sub(impact, this.center))

        return intersect(tmin, impact, normal)