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

maxRecursionDepth = 3

class Raytracer(object):
    def __init__(this, width, height, density = 1) -> None:
        this.width = width
        this.height = height
        this.scene = []
        this.clearColor = material((0, 0, 0))
        this.currentColor = material((255, 255, 255))
        this.lightSource = light((0, 0, 0), 1, (255, 255, 255))
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
        this.lightSource = light((position), intensity, diffuse)

    def reflect(this, direction, normal):
        return (sub(direction, mul(normal, 2 * dot(direction, normal))))

    def sceneIntersect(this, orig, direction):
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

    def castRay(this, orig, direction, recursion = 0):
        newMaterial, newIntersect = this.sceneIntersect(orig, direction)

        if recursion == maxRecursionDepth:
            return newMaterial, newIntersect

        if newIntersect:
            lightDir = norm(sub(this.lightSource.getPosition(), newIntersect.getPoint()))

            diffuseIntensity = dot(lightDir, newIntersect.getNormal())

            if diffuseIntensity > 0:
                diffuse = newMaterial.getColor() * diffuseIntensity * newMaterial.getAlbedo()[0]

                reflection = this.reflect(lightDir, newIntersect.getNormal())
                reflectionIntensity = max(dot(reflection, direction), 0)
                specularIntensity = this.lightSource.getIntensity() * reflectionIntensity ** newMaterial.spec
                specular = this.lightSource.getColor() * specularIntensity * newMaterial.getAlbedo()[1]

                offsetNormal = mul(newIntersect.getNormal(), 1.1)
                shadowOrigin = sub(newIntersect.getPoint(), offsetNormal) if diffuseIntensity < 0 else sumV3(newIntersect.getPoint(), offsetNormal)
                shadowMaterial, shadowIntersect = this.sceneIntersect(shadowOrigin, lightDir)
                shadowIntensity = 0.7 if shadowIntersect else 1

                if len(newMaterial.getAlbedo()) > 2 and newMaterial.getAlbedo()[2] > 0:
                    reverse = mul(direction, -1)
                    reflectDir = this.reflect(reverse, newIntersect.getNormal())
                    reflectOrigin = sumV3(newIntersect.getPoint(), mul(newIntersect.getNormal(), 1.1))
                    reflectColor, reflectIntersect = this.sceneIntersect(reflectOrigin, reflectDir)
                    reflectColor = reflectColor.getColor() * newMaterial.getAlbedo()[2]

                    return ((diffuse + specular) * shadowIntensity + reflectColor)
                else:
                    return((diffuse + specular) * shadowIntensity)
            else:
                return this.clearColor.getColor()
        else:
            return(newMaterial.getColor())



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

                    newColor  = this.castRay(origin, direction)

                    this.point(x, y, newColor)


                    # if newIntersect:
                    #     lightDir = norm(sub(this.lightSource.getPosition(), newIntersect.getPoint()))

                    #     diffuseIntensity = dot(lightDir, newIntersect.getNormal())

                    #     if diffuseIntensity < 0:
                    #         this.point(x, y, this.clearColor.getColor())
                    #     else:
                    #         diffuse = newMaterial.getColor() * diffuseIntensity * newMaterial.getAlbedo()[0]

                    #         reflection = this.reflect(lightDir, newIntersect.getNormal())
                    #         reflectionIntensity = max(dot(reflection, direction), 0)
                    #         specularIntensity = this.lightSource.getIntensity() * reflectionIntensity ** newMaterial.spec
                    #         specular = this.lightSource.getColor() * specularIntensity * newMaterial.getAlbedo()[1]

                    #         offsetNormal = mul(newIntersect.getNormal(), 1.1)
                    #         shadowOrigin = sub(newIntersect.getPoint(), offsetNormal) if diffuseIntensity < 0 else sumV3(newIntersect.getPoint(), offsetNormal)
                    #         shadowMaterial, shadowIntersect = this.castRay(shadowOrigin, lightDir)
                    #         shadowIntensity = 0.7 if shadowIntersect else 1

                    #         if len(newMaterial.getAlbedo()) > 2:
                    #             if newMaterial.getAlbedo()[2] > 0:
                    #                 reverse = mul(direction, -1)
                    #                 reflectDir = this.reflect(reverse, newIntersect.getNormal())
                    #                 reflectOrigin = sumV3(newIntersect.getPoint(), mul(newIntersect.getNormal(), 1.1))
                    #                 reflectColor, reflectIntersect = this.castRay(reflectOrigin, reflectDir)
                    #                 reflectColor = reflectColor.getColor() * newMaterial.getAlbedo()[2]
                    #             else:
                    #                 reflectColor = color(0, 0, 0)

                    #             this.point(x, y, (diffuse + specular) * shadowIntensity + reflectColor)
                    #         else:
                    #             this.point(x, y, (diffuse + specular) * shadowIntensity)
                    # else:
                    #     this.point(x, y, newMaterial.getColor())