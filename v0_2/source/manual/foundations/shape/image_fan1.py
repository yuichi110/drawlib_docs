from drawlib.apis import *

config(width=100, height=50, grid_only=True)
fan(xy=(25, 25), radius=15, from_angle=0, to_angle=135)
fan(xy=(75, 25), radius=20, from_angle=0, to_angle=135, angle=45, text="fan")
save()
