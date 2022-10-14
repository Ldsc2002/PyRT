from PyRT.driver import *

mirror = material("white", [0.1, 1, 0.8], 100)
glossRed = material("red", [0.9, 0.1], 10)
glass = material("white", [0, 0.5, 0.1, 0.8], 125, 1.5)

objects = [    
    sphere((0, -1.5, -10), 1.5, mirror),
    sphere((-2, -1, -12), 2, glossRed),
    sphere((1, 1, -8), 1.7, glass),
    sphere((-2, 2, -10), 2, mirror),
    plane((0, 4, -10), 6, 6, mirror)
]

setLight((-20, 20, 20), 2, "white")
addToScene(objects)
clear("grey")
render("rt")