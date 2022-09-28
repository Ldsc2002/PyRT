from PyRT.driver import *

if __name__ == "__main__":
    red = Material(color(255, 0, 0))

    objects = [        
        Sphere(V3(0, 3, -15), 3, red),
        Sphere(V3(0, 0, -10), 3, red)
    ]

    addToScene(objects)
    render()
    write()