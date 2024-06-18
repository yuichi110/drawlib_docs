from drawlib.apis import *

config(width=100, height=60, grid=True)

line((20, 10), (80, 10))
line(
    (20, 20),
    (80, 20),
    style=LineStyle(style="dashed", width=5, color=Colors.Red),
)
line((20, 30), (80, 30), arrowhead="->")
line((20, 40), (80, 40), arrowhead="<->")
line((20, 50), (80, 50), arrowhead="<-", style=LineStyle(ahscale=50, style="dashdot", ahfill=True))

save()
