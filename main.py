from PyRT.driver import *

if __name__ == "__main__":
    white = Material(color(255, 255, 255))
    red = Material(color(255, 0, 0))

    objects = [        
        Sphere(V3(0, 3, -15), 3, white),
        Sphere(V3(0, 0, -10), 3, red)
    ]

    addToScene(objects)
    render()
    write()