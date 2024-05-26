from drawlib.apis import *

c1 = Colors.get_rgba(rgb=Colors.Red, alpha=0.5)
print(c1)
# (255, 0, 0, 0.5)

c2 = Colors.get_rgba_from_hexcode(hexcode="#00FF00BB")
print(c2)
# (0, 255, 0, 0.7333333333333333)

c3 = Colors.get_rgba_from_hexcode(hexcode="#00FF00", alpha=0.7)
print(c3)
# (0, 255, 0, 0.7)

c4 = Colors.get_rgba_from_grayscale(grayscale=0.5, alpha=0.8)
print(c4)
# (127, 127, 127, 0.8)
