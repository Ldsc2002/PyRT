from PyRT.lib.utils import *
from PyRT.components.color import *

class material(object):
    def __init__(this, diffuse = color(255, 255, 255), albedo = [1, 0, 0, 0], spec = 0) -> None:
        this.diffuse = diffuse
        this.albedo = albedo
        this.spec = spec

    def getColor(this) -> color:
        return this.diffuse

    def getAlbedo(this) -> list:
        return this.albedo

    def getSpec(this) -> int:
        return this.spec