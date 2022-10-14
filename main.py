from PyRT.driver import *

mirror = material("white", [0.1, 1, 0.8], 100)
glossRed = material("red", [0.9, 0.1], 10)
glass = material("white", [0, 0.5, 0.1, 0.8], 125, 1.5)

objects = [    
    sphere((0, -1.5, -10), 1.5, mirror),
    cube((-2, 0, -10), 1, glossRed),
]

setLight((-20, 20, 20), 2, "white")
addToScene(objects)
clear("grey")
render("rt")