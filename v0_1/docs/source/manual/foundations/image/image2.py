from drawlib.apis import *

config(width=100, height=50, grid_only=True)

image(
    xy=(10, 25),
    width=10,
    image="python-logo-notext.png",
    style=ImageStyle(halign="left", valign="bottom"),
)
circle((10, 25), radius=0.5, style=ShapeStyle(fcolor=Colors.Red, lcolor=Colors.Red))
text((15, 20), "align: left,bottom")

image(
    xy=(40, 25),
    width=20,
    image="python-logo-notext.png",
    style=ImageStyle(lwidth=2, lstyle="dashed", lcolor=Colors.Red),
)
text((40, 10), "border: red,dot,width2")

image(xy=(75, 25), width=30, image="python-logo-notext.png", angle=45)
text((75, 5), "angle: 45")

save()
