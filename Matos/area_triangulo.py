import math

def areaTriangulo(a, b, c):

    p = (a + b + c) / 2

    area = round(math.sqrt((p * (p - a)) * ((p - b)) * ((p - c))))

    return area

print(areaTriangulo(9, 10, 14))