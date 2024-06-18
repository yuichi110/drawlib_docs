from drawlib.apis import *

config(width=100, height=60, grid=True)


image(xy=(25, 30), width=20, image="python.png")

dimg = Dimage("python.png").mirror().sepia()
image(xy=(75, 30), width=20, image=dimg)

save()
