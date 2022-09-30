from PyRT.lib.rt import *

RT = None

def checkInstanceOnCall(function):
    if RT is None: init()
    return function

def init(width: int = 1000, height: int = 1000, intensity = 1) -> None:
    global RT
    RT = Raytracer(width, height, intensity)
    RT.clear()

@checkInstanceOnCall
def point(x: int, y: int, color = None) -> None:
    RT.point(x, y, color)

@checkInstanceOnCall
def render(density = None) -> None:
    if density:
        RT.setDensity(density)
        
    RT.render()

@checkInstanceOnCall
def write(filename = "rt") -> None:
    RT.write(filename)

@checkInstanceOnCall
def addToScene(object) -> None:
    if isinstance(object, list):
        for item in object:
            RT.addToScene(item)
    else:
        RT.addToScene(object)