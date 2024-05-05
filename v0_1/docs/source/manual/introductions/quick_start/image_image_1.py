from drawlib.apis import *

config(width=100, height=60)

image(xy=(25, 30), width=20, image="python-logo-notext.png")
image(
    xy=(75, 30), 
    width=20, 
    angle=45, 
    image="python-logo-notext.png", 
    style=ImageStyle(lwidth=1)
)

save()
