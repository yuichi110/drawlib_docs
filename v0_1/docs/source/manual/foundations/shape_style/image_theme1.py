from drawlib.apis import *

dtheme.apply_official_theme("default2")
config(width=150, height=50)

# left
circle(
    xy=(25, 25),
    radius=15,
    style="red_flat",
    text="circle",
    textstyle="white",
)

# center
circle(
    xy=(75, 25),
    radius=15,
    style="blue_solid",
    text="circle",
    textstyle="blue_bold",
)

# right
circle(
    xy=(125, 25),
    radius=15,
    style="green_dashed_thin",
    text="circle",
    textstyle="green_thin",
)
save()
