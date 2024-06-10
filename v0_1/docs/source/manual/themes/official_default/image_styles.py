from drawlib.apis import *

# Changing theme to "default" is optional.
dtheme.apply_official_theme("default")

config(width=100, height=50)
start_x = 10
pad_x = 16
icon_y = 43
line_y = 36
rect_y = 27
image_y = 13
text_y = 5

rectangle(
    (82, 0),
    width=18,
    height=50,
    style=ShapeStyle(halign="left", valign="bottom", lwidth=0, fcolor=Colors140.LightGray),
)

colors = dtheme.colors.list()
colors.insert(0, "")
for i, style_name in enumerate(colors):
    x = start_x + pad_x * i
    t = style_name if style_name != "" else "(default)"

    icon_phosphor.heart((x, icon_y), width=10, style=style_name)
    line((x - 5, line_y), (x + 5, line_y), style=style_name)
    rectangle((x, rect_y), width=12, height=12, style=style_name)
    image((x, image_y), 10, "../python.png", style=style_name)
    text((x, text_y), t, style=style_name)

save()
