from drawlib.apis import *

config(width=100, height=100, dpi=200, grid=True)
circle(
    (50, 50),
    radius=30,
    text="(50,50)",
    textstyle=ShapeTextStyle(size=36),
)
save()
