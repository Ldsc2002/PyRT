from PyRT.lib.utils import *
from PyRT.figures.sphere import *
from PyRT.figures.cube import *
from PyRT.figures.plane import * 
from PyRT.figures.triangle import *
from PyRT.figures.pyramid import *
from PyRT.figures.obj import *
from PyRT.components.material import *
from PyRT.components.intersect import *
from PyRT.components.light import *
from PyRT.components.color import *
from random import uniform
from math import sqrt

importDependency("tqdm")
from tqdm import tqdm

class Raytracer(object):
    def __init__(this, width, height, density = 1) -> None:
        this.width = width
        this.height = height
        this.scene = []
        this.clearColor = material((0, 0, 0))
        this.currentColor = material((255, 255, 255))
        this.lightSource = light((0, 0, 0), 1, (255, 255, 255))
        this.density = density
        this.maxRecursionDepth = 3
        this.envMap = None

    def setRecursionDepth(this, depth: int) -> None:
        this.maxRecursionDepth = depth

    def addToScene(this, object) -> None:
        this.scene.append(object)

    def setClearColor(this, color) -> None:
        this.clearColor = material(color)

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

    def refract(this, direction, normal, ior):
        etai = 1
        etat = ior
        cosi = (dot(direction, normal) * -1)

        if cosi < 0:
            cosi = -cosi
            etai = etai * -1
            etat = etat * -1
            normal = mul(normal, -1)

        eta = etai / etat
        k = 1 - eta ** 2 * (1 - cosi ** 2)

        if k < 0:
            return color(0, 0, 0)

        else: 
            return norm(sumV3(mul(direction, eta), mul(normal, (eta * cosi - sqrt(k)))))

    def sceneIntersect(this, orig, direction):
        zbuffer = float('inf')
        newMaterial = this.clearColor
        newIntersect = None
        
        if this.envMap:
            newMaterial = this.envMap.getColor(direction)

        for object in this.scene:
            tempIntersect = object.figureIntersect(orig, direction)

            if tempIntersect and tempIntersect.getDistance() < zbuffer:
                newIntersect = tempIntersect
                zbuffer = newIntersect.getDistance()

                newMaterial = object.getMaterial()

        return newMaterial, newIntersect

    def castRay(this, orig, direction, recursion = 0):
        newMaterial, newIntersect = this.sceneIntersect(orig, direction)

        if recursion == this.maxRecursionDepth:
            return newMaterial.getColor()

        if newIntersect:
            lightDir = norm(sub(this.lightSource.getPosition(), newIntersect.getPoint()))

            diffuseIntensity = dot(lightDir, newIntersect.getNormal())
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
                reflectDir = this.reflect(direction, newIntersect.getNormal())
                reflectBias = 1.1 if dot(reflectDir, newIntersect.getNormal()) < 0 else -1.1
                reflectOrigin = sumV3(newIntersect.getPoint(), mul(newIntersect.getNormal(), reflectBias))
                reflectColor = this.castRay(reflectOrigin, reflectDir, recursion + 1)
                reflectColor = reflectColor * newMaterial.getAlbedo()[2]
            else:
                reflectColor = color(0, 0, 0)

            if len(newMaterial.getAlbedo()) > 3 and newMaterial.getAlbedo()[3] > 0:
                refractDir = this.refract(direction, newIntersect.getNormal(), newMaterial.getRefract())
                refractBias = -0.5 if dot(refractDir, newIntersect.getNormal()) < 0 else 0.5
                refractOrigin = sumV3(newIntersect.getPoint(), mul(newIntersect.getNormal(), refractBias))
                refractColor = this.castRay(refractOrigin, refractDir, recursion + 1)
                refractColor = refractColor * newMaterial.getAlbedo()[3]
            else:
                refractColor = color(0, 0, 0)

            return ((diffuse + specular) * shadowIntensity + reflectColor + refractColor)
      
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