from PyRT.lib.utils import *
from PyRT.figures.sphere import *
from PyRT.figures.cube import *
from PyRT.components.material import *
from PyRT.components.intersect import *
from PyRT.components.light import *
from PyRT.components.color import *
from random import uniform

importDependency("tqdm")
from tqdm import tqdm


class Raytracer(object):
    def __init__(this, width, height, density = 1) -> None:
        this.width = width
        this.height = height
        this.scene = []
        this.clearColor = material((0, 0, 0))
        this.currentColor = material((255, 255, 255))
        this.light = light(V3(0, 0, 0), 1, (255, 255, 255))
        this.density = density

    def addToScene(this, object) -> None:
        this.scene.append(object)

    def clear(this) -> None:
        this.framebuffer = [
            [this.clearColor.getColor().toBytes() for y in range(this.height)]
            for x in range(this.width)
        ]

    def point(this, x: int, y: int, diffuse = None) -> None:
        if y >= 0 and y < this.height and x >= 0 and x < this.width:
            this.framebuffer[x][y] = diffuse.toBytes() or this.currentColor.getColor().toBytes()

    def write(this, filename = "rt") -> None:
        writeBMP(this.framebuffer, filename)

    def setDensity(this, density) -> None:
        this.density = density

    def setLight(this, position = (0, 0, 0), intensity = 1, diffuse = (255, 255, 255)) -> None:
        this.light = light(V3(*position), intensity, diffuse)

    def render(this) -> None:
        fov = int(pi/2)
        aspectRatio = this.width / this.height

        for y in tqdm (range (this.height), desc="Rendering..."):
            for x in range(this.width):
                if uniform(0, 1) < this.density:
                    i = (2 * (x + 0.5) / this.width - 1) * tan(fov / 2) * aspectRatio
                    j = (1 - 2 * (y + 0.5) / this.height) * tan(fov / 2)

                    origin = V3(0, 0, 0)
                    direction = norm(V3(i, j, -1))

                    newMaterial, newIntersect  = this.castRay(origin, direction)

                    if newIntersect:
                        lightDir = norm(sub(this.light.getPosition(), newIntersect.getPoint()))

                        diffuseIntensity = dot(lightDir, newIntersect.getNormal())
                        diffuse = newMaterial.getColor() * diffuseIntensity * newMaterial.getAlbedo()[0]

                        reflection = this.reflect(lightDir, newIntersect.getNormal())
                        reflectionIntensity = max(dot(reflection, direction), 0)
                        specularIntensity = this.light.getIntensity() * reflectionIntensity ** newMaterial.spec
                        specular = this.light.getColor() * specularIntensity * newMaterial.getAlbedo()[1]

                        this.point(x, y, diffuse + specular)
                    else:
                        this.point(x, y, newMaterial.getColor())

    def reflect(this, direction, normal):
        return (sub(direction, mul(normal, 2 * dot(direction, normal))))

    def castRay(this, orig, direction):
        zbuffer = float('inf')
        newMaterial = this.clearColor
        newIntersect = None

        for object in this.scene:
            tempIntersect = object.intersect(orig, direction)

            if tempIntersect and tempIntersect.getDistance() < zbuffer:
                newIntersect = tempIntersect
                zbuffer = newIntersect.getDistance()

                newMaterial = object.getMaterial()

        return newMaterial, newIntersect