from PyRT.components.material import *

class figure(object): 
    def __init__(this, material) -> None:
        this.material = material

    def getMaterial(this) -> material:
        return this.material