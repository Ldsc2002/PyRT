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
def point(x: int, y: int, diffuse = None) -> None:
    RT.point(x, y, diffuse)

@checkInstanceOnCall
def render(name = None, density = None) -> None:
    if density:
        RT.setDensity(density)
        
    RT.render()

    if name:
        RT.write(name)

@checkInstanceOnCall
def write(filename = "rt") -> None:
    RT.write(filename)

@checkInstanceOnCall
def addToScene(object, translation = None) -> None:
    if isinstance(object, list):
        if translation:
            for obj in object:
                obj.translate(translation)

        for item in object:
            RT.addToScene(item)
    else:
        if translation:
            object.translate(translation)

        RT.addToScene(object)

@checkInstanceOnCall
def setLight(position = (0, 0, 0), intensity = 1, diffuse = (255, 255, 255)) -> None:
    RT.setLight(position, intensity, diffuse)

@checkInstanceOnCall
def clear(color = None) -> None:
    if color:
        RT.setClearColor(color)

    RT.clear()