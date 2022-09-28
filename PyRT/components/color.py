from PyRT.lib.utils import *

class color(object):
    def __init__(this, r, g, b) -> None:
        this.r = r
        this.g = g
        this.b = b

    def __add__(this, other):
        return color(
            this.r + other.r,
            this.g + other.g,
            this.b + other.b
        )

    def __mul__(this, other):
        if type(other) is color:
            return color(
                this.r * other.r,
                this.g * other.g,
                this.b * other.b
            )
        else:
            return color(
                this.r * other,
                this.g * other,
                this.b * other
            )

    def toBytes(this) -> bytes:
        return bytes([int(this.b), int(this.g), int(this.r)])