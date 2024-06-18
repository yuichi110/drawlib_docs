from drawlib.apis import *

config(width=100, height=60, grid=True)

star((25, 30), num_vertex=5, radius_ext=20, radius_int=7.5)
rectangle((75, 30), width=30, height=20, r=3, angle=45)

save()
