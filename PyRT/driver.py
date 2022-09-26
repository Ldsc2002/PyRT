from PyRT.lib.rt import *

RT = None

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