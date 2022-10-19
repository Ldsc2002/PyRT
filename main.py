from PyRT.driver import *

dirt = material("saddlebrown", [0.9, 0.1], 10)
grass = material("limegreen", [0.9, 0.1], 10)

clear("skyblue")
# objects = [    
#     cube((-3, 2, -5), 1, dirt),
#     cube((-2, 2, -5), 1, dirt),
#     cube((-1, 2, -5), 1, dirt),
#     cube((0, 2, -5), 1, dirt),
#     cube((1, 2, -5), 1, dirt),
#     cube((2, 2, -5), 1, dirt),
#     cube((3, 2, -5), 1, dirt),

#     cube((-3, 1, -5), 1, dirt),
#     cube((-2, 1, -5), 1, dirt),
#     cube((-1, 1, -5), 1, dirt),
#     cube((0, 1, -5), 1, dirt),
#     cube((1, 1, -5), 1, dirt),
#     cube((2, 1, -5), 1, dirt),
#     cube((3, 1, -5), 1, dirt),
# ]

objects = [
    obj("PyRT/assets/cubito.obj", dirt, (0, 0, -10)),
]

# objects = [
#     triangle([(0, 0, -10), (0, 1, -10), (1, 0, -10)], dirt),
#     triangle([(1, 0, -10), (2, 0, -10), (2, 1, -10)], dirt),

# ]

addToScene(objects)
render("rt")