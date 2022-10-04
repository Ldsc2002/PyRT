import struct
from collections import namedtuple
from math import cos, sin, tan
import importlib, os, sys

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])
V4 = namedtuple('Point4D', ['x', 'y', 'z', 'w'])
pi = 3.141592653589793238

def importDependency(moduleName:str) -> None:
    try:
        importlib.import_module(moduleName)
    except ImportError:
        print(moduleName + " not found, installing...")
        if os.system('PIP --version') == 0:
            os.system(f'PIP install {moduleName}')
        elif (os.system('pip3 --version') == 0):
            os.system(f'pip3 install {moduleName}')
        else:
            pip_location_attempt_1 = sys.executable.replace("python.exe", "") + "pip.exe"
            pip_location_attempt_2 = sys.executable.replace("python.exe", "") + "scripts\pip.exe"
            if os.path.exists(pip_location_attempt_1):
                os.system(pip_location_attempt_1 + " install " + moduleName)
            elif os.path.exists(pip_location_attempt_2):
                os.system(pip_location_attempt_2 + " install " + moduleName)
            else:
                print("Error: Unable to find PIP")
                print(f"You'll need to manually install the Module: {moduleName} in order for this program to work.")
                exit()
            
importDependency("matplotlib")
from matplotlib import colors

def sumV3(v0, v1):
    if type(v0) == V3:
        return V3(
            v0.x + v1.x,
            v0.y + v1.y,
            v0.z + v1.z
        )
    else:
        return V3(
            v0.x + v1,
            v0.y + v1,
            v0.z + v1,
        )

def sub(v0, v1):
    if type(v0) == V3:
        return V3(
            v0.x - v1.x,
            v0.y - v1.y,
            v0.z - v1.z
        )
    else:
        return V3(
            v0.x - v1,
            v0.y - v1,
            v0.z - v1,
        )

def mul(v0, k):
    return V3(v0.x * k, v0.y * k, v0.z *k)

def dot(v0, v1):
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v0, v1): 
	cx = v0.y * v1.z - v0.z * v1.y
	cy = v0.z * v1.x - v0.x * v1.z
	cz = v0.x * v1.y - v0.y * v1.x
	return V3(cx, cy, cz)

def length(v0):
    return (v0.x**2 + v0.y**2 + v0.z**2)**0.5

def norm(v0):
    l = length(v0)

    if l == 0:return V3(0, 0, 0)

    return V3(
		v0.x/l,
		v0.y/l,
		v0.z/l
	)

def bbox(A, B, C):
	xs = [A.x, B.x, C.x]
	xs.sort()
	ys = [A.y, B.y, C.y]
	ys.sort()
	return xs[0], xs[-1], ys[0], ys[-1]

def barycentric(A, B, C, P):
    bary = cross(
        V3(C.x - A.x, B.x - A.x, A.x - P.x), 
        V3(C.y - A.y, B.y - A.y, A.y - P.y)
    )

    if abs(bary[2]) < 1:
        return -1, -1, -1  
        
    return (
        1 - (bary[0] + bary[1]) / bary[2], 
        bary[1] / bary[2], 
        bary[0] / bary[2]
    )

def productMatrix(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

def matrixDot(v1, v2):
     return sum([x*y for x,y in zip(v1, v2)])

def productMatrixVector(M, v):
    return [matrixDot(r,v) for r in M]

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h', w)

def doubleword(d):
    return struct.pack('=l', d)

def colorBytes(r, g, b):
    return bytes([b, g, r])

def getColorValues(name: str) -> tuple:
    newColor = colors.to_rgba(name)

    return (
        int(newColor[0] * 255),
        int(newColor[1] * 255),
        int(newColor[2] * 255)
    )

def writeBMP(pixels, name):
    # Prints the pixels to the screen
    width = len(pixels)
    height = len(pixels[0])
    
    name  = name + '.bmp'
    f = open(name, 'bw')

    # File header (14 bytes)
    f.write(char('B'))
    f.write(char('M'))
    f.write(doubleword(14 + 40 + width * height * 3))
    f.write(doubleword(0))
    f.write(doubleword(14 + 40))

    # Image header (40 bytes)
    f.write(doubleword(40))
    f.write(doubleword(width))
    f.write(doubleword(height))
    f.write(word(1))
    f.write(word(24))
    f.write(doubleword(0))
    f.write(doubleword(width * height * 3))
    f.write(doubleword(0))
    f.write(doubleword(0))
    f.write(doubleword(0))
    f.write(doubleword(0))

    for y in range (0, height):
        for x in range (0, width):
            f.write(pixels[x][y])

    f.close()
    print('Image saved as ' + name)