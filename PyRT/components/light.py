from PyRT.lib.utils import *

class light(object):
    def __init__(this, position, intensity) -> None:
        this.position = position
        this.intensity = intensity

    def getPosition(this) -> V3:
        return this.position

    def getIntensity(this) -> float:
        return this.intensity