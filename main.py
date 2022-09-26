from PyRT.driver import *

if __name__ == "__main__":
    objects = [
        Sphere(V3(0.5, -4.25, -15), 0.2, color(77, 166, 255)),
        Sphere(V3(-0.5, -4.25, -15), 0.2, color(77, 166, 255)),

        Sphere(V3(0, -3.75, -15), 0.15, color(255, 153, 0)),

        Sphere(V3(0, -0.5, -15), 0.3, color(0, 13, 26)),
        Sphere(V3(0, -1.5, -15), 0.3, color(0, 13, 26)),

        Sphere(V3(0, 3, -15), 3),
        Sphere(V3(0, -1, -15), 2),
        Sphere(V3(0, -4, -15), 1.5)
    ]

    addToScene(objects)
    render()
    write()