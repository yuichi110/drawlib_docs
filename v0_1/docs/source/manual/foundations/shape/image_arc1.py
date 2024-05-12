from drawlib.apis import *

config(width=100, height=50, grid_only=True)
arc(xy=(25, 25), width=30, height=20, from_angle=0, to_angle=135)
arc(
    xy=(75, 25),
    width=40,
    height=30,
    from_angle=0,
    to_angle=135,
    angle=45,
    text="arc",
)
save()
