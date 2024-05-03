from drawlib.apis import *

config(width=100, height=100, dpi=200, grid=True)

align_leftbottom = ImageStyle(halign="left", valign="bottom")
image((0, 0), image="100px.png", width=10, style=align_leftbottom)
image((10, 0), image="200px.png", width=20, style=align_leftbottom)
image((30, 0), image="300px.png", width=30, style=align_leftbottom)
image((60, 0), image="400px.png", width=40, style=align_leftbottom)

image((0, 50), image="400px.png", width=10, style=align_leftbottom)
image((10, 50), image="300px.png", width=20, style=align_leftbottom)
image((30, 50), image="200px.png", width=30, style=align_leftbottom)
image((60, 50), image="100px.png", width=40, style=align_leftbottom)

save()
