from math import pi


def get_circle_area(r):
    if r < 0:
        return -1
    
    return r**2 * pi


def get_triangle_area(a, b, c):
    if any([i < 0 for i in [a, b, c]]):
        return -1
    
    sides = sorted([a, b, c])

    if sides[2] ** 2 == sides[0] ** 2 + (sides[2] - sides[0]) ** 2:
        return sides[0] * sides[1] / 2
    
    p_half =  (a + b + c) / 2
    return (p_half * (p_half - a) * (p_half - b) * (p_half - c)) ** 0.5
