from pyray import Color

def MakeColorFromRGB(r : int, g : int, b : int):
    col = Color(r, g, b, 255)
    return col

def MakeColorFromRGBA(r : int, g : int, b : int, a : int):
    col = Color(r, g, b, a)
    return col
