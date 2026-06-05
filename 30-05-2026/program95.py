import math
def area_of_hexagon(X):
    area = (3 * math.sqrt(3) * (X ** 2)) / 2
    return round(area, 1)
print(area_of_hexagon(5))
print(area_of_hexagon(10))
print(area_of_hexagon(15))
