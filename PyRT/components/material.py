from PyRT.lib import utils
from PyRT.components.color import *

class material(object):
    def __init__(this, diffuse, albedo = [1, 0, 0, 0], spec = 0) -> None:
        if type(diffuse) is str:
            this.diffuse = utils.getColor(diffuse)
        else:
            this.diffuse = diffuse
        
        this.albedo = albedo
        this.spec = spec

    def getColor(this) -> color:
        return this.diffuse

    def getAlbedo(this) -> list:
        return this.albedo

    def getSpec(this) -> int:
        return this.spec