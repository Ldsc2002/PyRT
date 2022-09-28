from PyRT.driver import *

if __name__ == "__main__":
    white = material(color(255, 255, 255))
    red = material(color(255, 0, 0))

    objects = [      
        cube((0, 0, -8), 2, white),  
        sphere((0, 3, -15), 3, white),
        sphere((0, 0, -10), 2, red)
    ]

    addToScene(objects)
    render()
    write()