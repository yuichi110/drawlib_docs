from drawlib.apis import *

config(width=100, height=50, grid_only=True)
arc(xy=(25, 25), width=30, height=20, theta_begin=0, theta_end=135)
arc(xy=(75, 25), width=40, height=30, theta_begin=0, theta_end=135, angle=45, text="arc")
save()
