from drawlib.apis import *

config(width=100, height=100)
circle(
    xy=(50, 50),
    radius=30,
    style=ShapeStyle(
        lstyle="dashed",
        lcolor=Colors140.BlueViolet,
        lwidth=5,
        fcolor=Colors140.Turquoise,
    ),
)
save()
