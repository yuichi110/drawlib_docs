from drawlib.apis import *

config(width=100, height=50)

print(dtheme.colors.list())
# ['default', 'blue', 'blue1', 'blue2', 'green', 'green1', 'green2',
# 'pink', 'pink1', 'pink2', 'black', 'black1', 'black2', 'white']

print(dtheme.colors.get("blue"))
# (109, 124, 197, 1.0)

print(dtheme.colors.get("blue1"))
# (18, 21, 43, 1.0)

print(dtheme.colors.get("blue2"))
# (109, 124, 197, 1.0)
