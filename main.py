from PyRT.driver import *

if __name__ == "__main__":
    objects = [      
        cube((0, 0, -8), 2, getColor("red")),  
        sphere((0, 3, -15), 3, getColor("green")),
        sphere((0, 0, -10), 2, getColor("blue")),
    ]

    addToScene(objects)
    render()
    write()