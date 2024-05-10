from drawlib.apis import *

config(width=100, height=50, grid_only=True)
wedge(xy=(25, 25), radius=15, width=5, theta_begin=0, theta_end=135)
wedge(xy=(75, 25), radius=20, width=10, theta_begin=0, theta_end=135, angle=45, text="wedge")
save()
