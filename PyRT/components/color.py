from PyRT.lib.utils import *

class color(object):
    def __init__(this, r, g, b) -> None:
        this.r = r
        this.g = g
        this.b = b

    def __add__(this, other):
        if type(other) is color:
            return color(
                min((this.r + other.r), 255),
                min((this.g + other.g), 255),
                min((this.b + other.b), 255)
            )
        else:
            return color(
                min((this.r + other), 255),
                min((this.g + other), 255),
                min((this.b + other), 255)
            )

    def __mul__(this, other):
        if type(other) is color:
            return color(
                min((this.r * other.r), 255),
                min((this.g * other.g), 255),
                min((this.b * other.b), 255)
            )
        else:
            return color(
                min((this.r * other), 255),
                min((this.g * other), 255),
                min((this.b * other), 255)
            )

    def toBytes(this) -> bytes:
        return bytes([int(this.b), int(this.g), int(this.r)])