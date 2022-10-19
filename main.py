from PyRT.driver import *

sand = material("darkkhaki", [0.9, 0.1], 0)
rock = material("dimgray", [0.9, 0.1], 0)
dirt = material("saddlebrown", [0.9, 0.1], 0)
cactus = material("darkgreen", [0.9, 0.1], 0)
water = material("blue", [0, 0.5, 0.1, 0.8], 10, 1.5)

setEnvMap("PyRT/assets/minecraft.bmp")

clear("skyblue")
objects = [    
    cube((-3, 2, -5),  1, rock),
    cube((-2, 2, -5), 1, rock),
    cube((-1, 2, -5), 1, rock),
    cube((0, 2, -5), 1, rock),
    cube((1, 2, -5), 1, rock),
    cube((2, 2, -5), 1, rock),
    cube((3, 2, -5), 1, rock),

    cube((-3, 1, -5), 1, water),
    cube((-2, 1, -5), 1, water),
    cube((-1, 1, -5), 1, water),
    cube((0, 1, -5), 1, sand),
    cube((1, 1, -5), 1, sand),
    cube((2, 1, -5), 1, sand),
    cube((3, 1, -5), 1, sand),

    cube((2, 0, -5), 1, dirt),
    cube((3, 0, -5), 1, dirt),

    obj("PyRT/assets/cactus.obj", cactus, (0.5, -1.5, -5), (0.5, 0.5, 0.5))
]

addToScene(objects)
render("rt")