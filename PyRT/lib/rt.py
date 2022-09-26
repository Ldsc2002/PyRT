from PyRT.lib.utils import *
from PyRT.components.sphere import *

class Raytracer(object):
    def __init__(this, width, height) -> None:
        this.width = width
        this.height = height
        this.scene = []
        this.clearColor = color(0, 0, 0)
        this.currentColor = color(255, 255, 255)

    def addToScene(this, object) -> None:
        this.scene.append(object)

    def clear(this) -> None:
        this.framebuffer = [
            [this.clearColor for x in range(this.width)]
            for y in range(this.height)
        ]

    def point(this, x: int, y: int, color = None) -> None:
        if y >= 0 and y < this.height and x >= 0 and x < this.width:
            this.framebuffer[y][x] = color or this.currentColor

    def write(this, filename = "rt") -> None:
        writeBMP(this.framebuffer, filename)

    def render(this) -> None:
        fov = int(pi/2)
        aspectRatio = this.width / this.height

        for y in range(this.height):
            for x in range(this.width):
                i = (2 * (x + 0.5) / this.width - 1) * tan(fov / 2) * aspectRatio
                j = (1 - 2 * (y + 0.5) / this.height) * tan(fov / 2)

                origin = V3(0, 0, 0)
                direction = norm(V3(i, j, -1))

                c = this.castRay(origin, direction)
                this.point(x, y, c)

    def castRay(this, orig, direction) -> color:
        for object in this.scene:
            if object.intersect(orig, direction):
                return object.getColor()

        return this.clearColor