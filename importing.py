#sarah verburg 06-06

from bad_code import area_square

area = area_square(40)
print(area)

print("Global namespace")
namespace = globals().copy()

for name, obj in namespace.items() :
    print(name, object)
