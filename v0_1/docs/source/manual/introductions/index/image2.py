from drawlib.apis import *

# define this code at style.py normally
dtheme.apply_official_theme("simple")
dtheme.allstyles.merge(
    dtheme.ThemeStyles(
        textstyle=TextStyle(font=FontSansSerif.RALEWAYS_REGULAR, size=20),
    )
)

# import style at illustration code normaly
config(width=100, height=50)
xs = [10, 30, 50, 70, 90]
y_text = 4
y_image = 15
y_shape = 35
y_line = 46

rectangle(
    (60, 0),
    width=20,
    height=50,
    style=ShapeStyle(halign="left", valign="bottom", fcolor=Colors140.LightGray, lwidth=0),
)
rectangle(
    (80, 0),
    width=20,
    height=50,
    style=ShapeStyle(halign="left", valign="bottom", fcolor=Colors140.DarkGray, lwidth=0),
)

for i, style in enumerate(["", "blue_flat", "green_solid", "pink_dashed", "white"]):
    x = xs[i]

    # draw text
    if dtheme.textstyles.has(style):
        if style == "":
            text((x, y_text), "(default)", style=style)
        else:
            text((x, y_text), style, style=style)
    else:
        text((x, y_text), style, style=style.split("_")[0])

    # draw image
    if i == 1:
        image((x, y_image), width=12, image="python.png", angle=30, style=style)
    else:
        image((x, y_image), width=12, image="python.png", style=style)

    if i == 0:
        circle((x, y_shape), radius=6, text="circle")
        line((x - 5, y_line), (x + 5, y_line))
    elif i == 1:
        rectangle((x, y_shape), width=12, height=12, angle=30, style=style, text="rect", textstyle="white")
    elif i == 2:
        arrow(
            (x - 7, y_shape),
            (x + 7, y_shape),
            head_width=10,
            head_length=5,
            head_style="-|>",
            tail_width=5,
            style=style,
            text="rarrow",
            textstyle="green",
        )
        line_curved((x - 5, y_line), (x + 5, y_line), bend=0.5, style=style)
    elif i == 3:
        star(
            (x, y_shape),
            num_vertex=5,
            radius_ext=8,
            radius_int=3,
            style=style,
            text="5star",
            textstyle="pink",
        )
        line_bezier1((x - 5, y_line + 2), (x + 5, y_line + 2), (x + 5, y_line - 2), style=style)
    else:
        arrow(
            (x - 7, y_shape),
            (x + 7, y_shape),
            head_width=15,
            head_length=5,
            head_style="<|-|>",
            tail_width=3,
            style=style,
            text="barrow",
            textstyle="blue",
        )
        line((x - 5, y_line), (x + 5, y_line), style=dtheme.linearrowstyles.get(f"{style}.200"))

save()
