import math


def polysum(n, s):
    """
    Input: number of sides: n, and length of each side: s
    Output: outputs the summed area and perimeter
    """
    area = (0.25 * n * s ^ 2)/math.tan(math.pi / n)
    perimeter = (n * s)**2
    return round(area + perimeter, 4)
