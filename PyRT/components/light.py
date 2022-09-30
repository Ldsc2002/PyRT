from PyRT.lib.utils import *

class light(object):
    def __init__(this, position, intensity, color) -> None:
        this.position = position
        this.intensity = intensity
        this.color = color

    def getColor(this) -> color:
        return this.color

    def getPosition(this) -> V3:
        return this.position

    def getIntensity(this) -> float:
        return this.intensity