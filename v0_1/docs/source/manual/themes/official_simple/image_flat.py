from drawlib.apis import *


def stuck1(xy, widths):
    for width in widths:
        rectangle(xy, width=width, height=width, style="blue_flat")


def stuck2(xy, repeat, width, shift):
    x, y = xy
    sx, sy = shift
    for i in range(repeat):
        x1 = x + i * sx
        y1 = y + i * sy
        rectangle((x1, y1), width=width, height=width, style="blue_flat")


dtheme.apply_official_theme("simple")
stuck1((25, 25), [20, 15, 10, 5])
stuck2((65, 15), 5, 10, (5, 5))

dtheme.shapestyles.merge(ShapeStyle(lwidth=0), ["blue_flat"])
stuck1((25, 75), [20, 15, 10, 5])
stuck2((65, 65), 5, 10, (5, 5))

save()
