from drawlib.apis import *

config(width=100, height=60)


image(xy=(25, 30), width=20, image="python-logo-notext.png")

dimg = Dimage("python-logo-notext.png").mirror().sepia()
image(xy=(75, 30), width=20, image=dimg)

save()
