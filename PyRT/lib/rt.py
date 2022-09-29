from PyRT.lib.utils import *
from PyRT.figures.sphere import *
from PyRT.figures.cube import *
from PyRT.components.material import *
from PyRT.components.intersect import *
from PyRT.components.light import *
from PyRT.components.color import *
from random import uniform

class Raytracer(object):
    def __init__(this, width, height, density = 1) -> None:
        this.width = width
        this.height = height
        this.scene = []
        this.clearColor = color(0, 0, 0)
        this.currentColor = color(255, 255, 255)
        this.light = light(V3(0, 0, 0), 1)
        this.density = density

    def addToScene(this, object) -> None:
        this.scene.append(object)

    def clear(this) -> None:
        this.framebuffer = [
            [this.clearColor.toBytes() for x in range(this.width)]
            for y in range(this.height)
        ]

    def point(this, x: int, y: int, color = None) -> None:
        if y >= 0 and y < this.height and x >= 0 and x < this.width:
            this.framebuffer[y][x] = color.toBytes() or this.currentColor.toBytes()

    def write(this, filename = "rt") -> None:
        writeBMP(this.framebuffer, filename)

    def setDensity(this, density) -> None:
        this.density = density

    def render(this) -> None:
        fov = int(pi/2)
        aspectRatio = this.width / this.height

        for y in range(this.height):
            for x in range(this.width):
                if uniform(0, 1) < this.density:
                    i = (2 * (x + 0.5) / this.width - 1) * tan(fov / 2) * aspectRatio
                    j = (1 - 2 * (y + 0.5) / this.height) * tan(fov / 2)

                    origin = V3(0, 0, 0)
                    direction = norm(V3(i, j, -1))

                    c, newIntersect  = this.castRay(origin, direction)

                    if newIntersect:
                        lightDir = norm(sub(this.light.getPosition(), newIntersect.getPoint()))
                        lightIntensity = dot(lightDir, newIntersect.getNormal())

                        diffuse = c * lightIntensity

                        this.point(x, y, diffuse)
                    else:
                        this.point(x, y, c)


    def castRay(this, orig, direction):
        zbuffer = float('inf')
        material = this.clearColor
        newIntersect = None

        for object in this.scene:
            tempIntersect = object.intersect(orig, direction)

            if tempIntersect and tempIntersect.getDistance() < zbuffer:
                newIntersect = tempIntersect
                zbuffer = newIntersect.getDistance()
                material = object.getMaterial().getColor()

        return material, newIntersect