from PyRT.driver import *

if __name__ == "__main__":
    rubber = material(color(255, 0, 0), [0.9, 0.1], 10)
    ivory = material(color(255, 255, 255), [0.6, 0.3], 50)

    objects = [      
        sphere((0, 3, -15), 3, rubber),
        sphere((0, 0, -10), 2, ivory),
    ]

    addToScene(objects)
    render()
    write()