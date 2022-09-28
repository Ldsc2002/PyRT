from PyRT.components.material import *

class Figure(object): 
    def __init__(this, material) -> None:
        this.material = material

    def getMaterial(this) -> Material:
        return this.material