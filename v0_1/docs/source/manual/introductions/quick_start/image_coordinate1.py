from drawlib.apis import *

config(width=100, height=60, grid_only=True)

circle(
    xy=(25, 30),
    radius=10,
    style=ShapeStyle(halign="center", valign="center"),
)
circle(
    xy=(25, 30),
    radius=1,
    style=ShapeStyle(fcolor=Colors.Red, lcolor=Colors.Red),
)
text((25, 10), "Align center,center", style=TextStyle(color=Colors.Red))

circle(
    xy=(75, 30),
    radius=10,
    style=ShapeStyle(halign="left", valign="bottom"),
)
circle(
    xy=(75, 30),
    radius=1,
    style=ShapeStyle(fcolor=Colors.Red, lcolor=Colors.Red),
)
text((75, 10), "Align left,bottom", style=TextStyle(color=Colors.Red))

save()
