import struct
from PyRT.components.material import material
from PyRT.lib.utils import *
from PyRT.components.color import color

class Envmap:
    def __init__(this, path):
        this.path = path
        this.read()
    
    def read(this):
        with open(this.path, "rb") as image:
            image.seek(2 + 4 + 4) 
            header_size = struct.unpack("=l", image.read(4))[0] 
            image.seek(2 + 4 + 4 + 4 + 4)
            
            this.width = struct.unpack("=l", image.read(4))[0]
            this.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)

            this.pixels = [
                [ bytes([0, 0, 0]) for y in range(this.height)]
                for x in range(this.width) 
            ]

            for y in reversed(range(this.height)):
                this.pixels.append([])
                for x in reversed(range(this.width)):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))

                    this.pixels[x][y] = ([r, g, b])


    def getColor(this, direction):
        direction = norm(direction)

        x = min((atan2(direction.z, direction.x) / (2 * pi) + 0.5)*2, 1)
        y = min((acos(-direction.y) / pi)*2, 1)

        x = max(min(x, 1), 0)
        y = max(min(y, 1), 0)

        x = int(x * this.width - 1)
        y = int(y * this.height - 1)

        return material(this.pixels[x][y])