import math

# tinh dien tich hinh tron
# ten function: area 
# input: radius(ban kinh)
# output: area 
def area(radius):
    area = (radius**2)*math.pi
    area_round = round(area, 2)
    return area_round
