from drawlib.apis import *

config(width=100, height=60, grid=True)

line((20, 10), (80, 10))
line_curved((20, 25), (80, 25), bend=0.2)
line_curved((20, 35), (80, 35), bend=-0.2)
lines([(20, 45), (30, 50), (70, 50), (80, 45)])

save()
