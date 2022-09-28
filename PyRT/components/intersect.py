from PyRT.lib.utils import *

class intersect(object):
    def __init__(this, distance, point, normal) -> None:
        this.distance = distance
        this.point = point
        this.normal = normal

    def getDistance(this) -> float:
        return this.distance

    def getPoint(this) -> V3:
        return this.point

    def getNormal(this) -> V3:
        return this.normal