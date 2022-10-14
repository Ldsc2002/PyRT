from PyRT.driver import *

mirror = material("white", [0.1, 1, 0.8], 100)
glossRed = material("red", [0.9, 0.1], 10)
glass = material("white", [0, 0.5, 0.1, 0.8], 125, 1.5)

objects = [    
    cube((-2, 0, -10), 1, glossRed),
    triangle(((-1, -1, -10), (1, -1, -10), (0, 1, -10)), mirror),
]

setLight((-20, 20, 20), 2, "white")
addToScene(objects)
clear("grey")
render("rt")