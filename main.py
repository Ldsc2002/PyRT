from PyRT.driver import *

whiteFur = material("white", [0.9, 0.1], 10)
glossWhite = material("white", [0.6, 0.3], 50)

orangeFur = material("peru", [0.9, 0.1], 10)
glossRed = material("red", [0.6, 0.3], 50)

glossBlack = material("black", [0.1, 0.9], 150)

whiteBear = [      
    sphere((0, 2, -15), 3, glossWhite),

    sphere((2, 0.75, -12), 1, whiteFur),
    sphere((-2, 0.75, -12), 1, whiteFur),
    sphere((2, 3.5, -12), 1, whiteFur),
    sphere((-2, 3.5, -12), 1, whiteFur),

    sphere((0, -1.5, -13), 2, whiteFur),
    sphere((1.5, -3, -12), 0.8, whiteFur),
    sphere((-1.5, -3, -12), 0.8, whiteFur),
    sphere((0, -1, -11.85), 1, whiteFur),

    sphere((0.6, -1.75, -11), 0.2, glossBlack),
    sphere((-0.6, -1.75, -11), 0.2, glossBlack),
    sphere((0, -0.9, -10.75), 0.2, glossBlack),
]

orangeBear = [      
    sphere((0, 2, -15), 3, glossRed),

    sphere((2, 0.75, -12), 1, orangeFur),
    sphere((-2, 0.75, -12), 1, orangeFur),
    sphere((2, 3.5, -12), 1, orangeFur),
    sphere((-2, 3.5, -12), 1, orangeFur),

    sphere((0, -1.5, -13), 2, orangeFur),
    sphere((1.5, -3, -12), 0.8, orangeFur),
    sphere((-1.5, -3, -12), 0.8, orangeFur),
    sphere((0, -1, -11.85), 1, orangeFur),

    sphere((0.6, -1.75, -11), 0.2, glossBlack),
    sphere((-0.6, -1.75, -11), 0.2, glossBlack),
    sphere((0, -0.9, -10.75), 0.2, glossBlack),
]

init(1920, 1080)
addToScene(whiteBear, (-3.5, 0, 0))
addToScene(orangeBear, (3.5, 0, 0))

render("bears")