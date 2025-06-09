#sarah verburg 06-06
"""Module for investigating importing and namespace"""

import better_code
from better_code import area_square

area = better_code.area_square(40)
area1 = area_square(40)
print(area1)

print("Global namespace")
namespace = globals().copy()

for name, obj in namespace.items() :
    print(name, object)
