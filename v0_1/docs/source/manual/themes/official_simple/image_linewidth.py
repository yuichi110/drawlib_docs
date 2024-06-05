from drawlib.apis import *

dtheme.apply_official_theme("simple")

config(width=100, height=50)
start_x = 15
pad_x = 18
circle_y = 30
line_y = 15
text_y = 10

for i, line_width_percent in enumerate(["", ".50", ".100", ".200", ".400"]):

    x = start_x + pad_x * i
    style = f"blue_solid{line_width_percent}"
    circle((x, circle_y), radius=7, style=style)
    line((x - 5, line_y), (x + 5, line_y), style=style)
    text((x, text_y), style)

save()
