#sarah verburg 06-06

# bad code
# area = 0
# def areaSquare(length):
#     area = length * length
#     return area
#
# areaSquare(30)
# print(area)

# good code
def area_square(length: float) -> float:
    return length * length

area = area_square(30)
print(area)
