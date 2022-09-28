from PyRT.lib.utils import *
from PyRT.components.intersect import *
from PyRT.components.material import *
from PyRT.figures.figure import *

class Cube(Figure): 
    def __init__(this, center, side, material) -> None:
        this.center = V3(*center)
        this.side = side
        this.material = material