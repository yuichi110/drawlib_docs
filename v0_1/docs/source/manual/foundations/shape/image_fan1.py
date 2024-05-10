from drawlib.apis import *

config(width=100, height=50, grid_only=True)
fan(xy=(25, 25), radius=15, theta_begin=0, theta_end=135)
fan(xy=(75, 25), radius=20, theta_begin=0, theta_end=135, angle=45, text="fan")
save()
