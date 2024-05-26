from drawlib.apis import *

config(width=100, height=50, dpi=200, background_color=Colors.Green)
tstyle = TextStyle(color=Colors.White)

# invert
image((20, 25), 20, Dimage("linux.png").invert())
text((20, 10), "invert()", style=tstyle)

# brightness
image((50, 25), 20, Dimage("linux.png").colorize(black="red", white="blue"))
text((50, 10), "colorize()", style=tstyle)

# invert (rectangle is just background)
image((80, 25), 20, Dimage("linux.png").posterize(4))
text((80, 10), "posterize()", style=tstyle)

save()
