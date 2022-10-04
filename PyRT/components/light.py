from PyRT.components.color import *
from PyRT.lib.utils import *

class light(object):
    def __init__(this, position, intensity = 1, diffuse = (255, 255, 255)) -> None:
        this.position = V3(*position)
        this.intensity = intensity
        this.diffuse = color(diffuse)

    def getColor(this) -> color:
        return this.diffuse

    def getPosition(this) -> V3:
        return this.position

    def getIntensity(this) -> float:
        return this.intensity