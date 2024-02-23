import math

def regular_polygon_area(n, s):
    cot_angle = math.cos(math.pi / n) / math.sin(math.pi / n)
    area = math.ceil(0.25 * n * s ** 2 / cot_angle)
    return area

num_sides = int(input("Sides of polygonn: "))
side_length = float(input("Length of polygon: "))

polygon_area = regular_polygon_area(num_sides, side_length)
print("Area of polygon:", polygon_area)