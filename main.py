from PyRT.driver import *

glossWhite = material("white", [0.9, 0.1], 10)
glossRed = material("red", [0.9, 0.1], 10)

objects = [      
    sphere((0, -1.5, -10), 1.5, glossWhite),
    sphere((-2, -1, -12), 2, glossRed),
    sphere((1, 1, -8), 1.7, glossRed),
    sphere((-2, 2, -10), 2, glossWhite),
]

addToScene(objects)
render("rt")