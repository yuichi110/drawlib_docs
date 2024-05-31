from drawlib.apis import *

dtheme.apply_official_theme("gray")

config(width=100, height=50)
circle((50, 25), radius=15)
save()

dtheme.apply_official_theme("default")
