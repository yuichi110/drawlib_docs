from drawlib.apis import *


dtheme.apply_official_theme("rich")

config(width=100, height=60)
start_x = 10
pad_x = 16


def draw_horizon(colors: list[str], y):
    rect_y = y
    text1_y = y - 4
    text2_y = y - 7

    for i, color_name in enumerate(colors):
        color = dtheme.colors.get(color_name)
        x = start_x + pad_x * i
        lwidth = 0 if color_name != "white" else 1
        rectangle(
            (x, rect_y),
            width=10,
            height=4,
            style=ShapeStyle(fcolor=color, lwidth=lwidth, lcolor=Colors.Black),
        )
        text((x, text1_y), color_name)
        text((x, text2_y), str(color[:3]), style=TextStyle(size=14))


draw_horizon(["turquoise", "green_sea", "emerald", "nephritis", "peter_river", "belize_hole"], 54)
draw_horizon(["amethyst", "wisteria", "wet_asphalt", "midnight_blue", "sun_flower", "orange"], 40)
draw_horizon(["carrot", "pumpkin", "alizarin", "pomegranate", "clouds", "silver"], 26)
draw_horizon(["concrete", "asbestos", "black", "white"], 12)
save()
