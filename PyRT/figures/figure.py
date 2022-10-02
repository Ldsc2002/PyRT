from PyRT.components.material import *
from PyRT.lib.utils import *
from PyRT.components.intersect import *
from PyRT.components.material import *

class figure(object): 
    def __init__(this, center, material) -> None:
        this.center = V3(*center)
        this.material = material

    def getMaterial(this) -> material:
        return this.material

    def translate(this, translation) -> None:
        this.center = sumV3(this.center, V3(*translation))

    