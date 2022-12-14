from PyRT.components.color import *

class material(object):
    def __init__(this, diffuse, albedo = [1, 0, 0, 0], spec = 0, refract = 0) -> None:
        this.diffuse = color(diffuse)       
        this.albedo = albedo
        this.spec = spec
        this.refract = refract

    def getColor(this) -> color:
        return this.diffuse

    def getAlbedo(this) -> list:
        return this.albedo

    def getSpec(this) -> int:
        return this.spec

    def getRefract(this) -> int:
        return this.refract