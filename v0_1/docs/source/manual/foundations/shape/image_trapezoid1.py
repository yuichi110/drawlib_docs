from drawlib.apis import *

config(width=100, height=50, grid_only=True)
trapezoid(xy=(25, 25), height=20, bottom_width=30, top_width=20)
trapezoid(
    xy=(75, 25),
    height=20,
    bottom_width=30,
    top_width=20,
    top_start=0,
    angle=45,
    text="trapezoid()",
)
save()
