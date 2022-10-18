from PyRT.figures.figure import *
from PyRT.figures.triangle import *

class obj(figure):
    def __init__(this, filename, material, center, scale = (1, 1 ,1)) -> None:
        this.filename = filename
        this.material = material
        this.center = V3(*center)
        this.scale = V3(*scale)
        this.vertices = []
        this.faces = []
        this.read()

    def read(this) -> None:
        with open(this.filename) as file:
            for line in file:
                if line:
                    prefix, value = line.split(' ', 1)

                    if prefix == 'v':
                        this.vertices.append(list(map(float, value.split(' '))))
                    elif prefix == 'f':
                        this.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])
        
        for i in range(len(this.vertices)):
            this.vertices[i] = V3(*this.vertices[i])
            this.vertices[i] = sumV3(this.vertices[i], this.center)

        for i in range(len(this.vertices)):
            this.vertices[i] = V3(*this.vertices[i])
            this.vertices[i] = mul(this.vertices[i], this.scale)

    def figureIntersect(this, orig, direction) -> intersect:
        tmin = float('inf')
        impact = None
        normal = None

        for face in this.faces:
            v1 = this.vertices[face[0][0] - 1]
            v2 = this.vertices[face[1][0] - 1]
            v3 = this.vertices[face[2][0] - 1]

            newTriangle = triangle([v1, v2, v3], this.material)
            newIntersect = newTriangle.figureIntersect(orig, direction)

            if newIntersect:
                if newIntersect.getDistance() < tmin:
                    tmin = newIntersect.getDistance()
                    impact = newIntersect.getPoint()
                    normal = newIntersect.getNormal()
                    
        if impact:
            return intersect(tmin, impact, normal)
        else:
            return None