from PyRT.lib.utils import getColorValues

class color(object):
    def __init__(this, r, g = None, b = None) -> None:
        if type(r) is str:
            tempColor = getColorValues(r)
            this.r = tempColor[0]
            this.g = tempColor[1]
            this.b = tempColor[2]
        elif type(r) is list or type(r) is tuple:
            this.r = r[0]
            this.g = r[1]
            this.b = r[2]
        else:
            this.r = r
            this.g = g
            this.b = b

    def __add__(this, other):
        if type(other) is color:
            return color(
                max(min((this.r + other.r), 255), 0),
                max(min((this.g + other.g), 255), 0),
                max(min((this.b + other.b), 255), 0)
            )
        else:
            return color(
                max(min((this.r + other), 255), 0),
                max(min((this.g + other), 255), 0),
                max(min((this.b + other), 255), 0)
            )

    def __mul__(this, other):
        if type(other) is color:
            return color(
                max(min((this.r * other.r), 255), 0),
                max(min((this.g * other.g), 255), 0),
                max(min((this.b * other.b), 255), 0)
            )
        else:
            return color(
                max(min((this.r * other), 255), 0),
                max(min((this.g * other), 255), 0),
                max(min((this.b * other), 255), 0)
            )

    def toBytes(this) -> bytes:
        return bytes([int(this.b), int(this.g), int(this.r)])