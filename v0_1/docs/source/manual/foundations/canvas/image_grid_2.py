from drawlib.apis import *

config(
    grid_style=LineStyle(
        width=1,
        color=Colors.Red,
        style="dashed",
    ),
    grid_centerstyle=LineStyle(
        width=2,
        color=Colors.Blue,
        style="dashed",
    ),
)

circle((50, 50), radius=30)
save()
