from PyRT.lib.rt import *

RT = None

colors = {
    "white": material(color(255, 255, 255)),
    "red": material(color(255, 0, 0)),
    "green": material(color(0, 255, 0)),
    "blue": material(color(0, 0, 255)),
    "black": material(color(0, 0, 0)),
    "yellow": material(color(255, 255, 0)),
    "cyan": material(color(0, 255, 255)),
    "magenta": material(color(255, 0, 255)),
    "grey": material(color(128, 128, 128)),
    "orange": material(color(255, 165, 0)),
    "purple": material(color(128, 0, 128)),
    "brown": material(color(165, 42, 42)),
    "pink": material(color(255, 192, 203)),
}

def checkInstanceOnCall(function):
    if RT is None: init()
    return function

def init(width: int = 1000, height: int = 1000) -> None:
    global RT
    RT = Raytracer(width, height)
    RT.clear()

@checkInstanceOnCall
def point(x: int, y: int, color = None) -> None:
    RT.point(x, y, color)

@checkInstanceOnCall
def render() -> None:
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

def getColor(color: str) -> material:
    return colors[color] if color in colors else colors["white"]

def addColor(name: str, color: material) -> None:
    colors[name] = color