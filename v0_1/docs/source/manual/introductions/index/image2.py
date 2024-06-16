from drawlib.apis import *


def main():
    for theme, styles in [
        ("default2", ["", "blue_flat", "green_solid", "red_dashed", "white"]),
        ("essentials", ["", "purple_flat", "teal_solid", "navy_dashed", "yellow"]),
        ("monochrome", ["", "black_flat", "silver_solid", "graphite_dashed", "white"]),
    ]:

        draw(theme, styles)
        save(f"image2_{theme}.png")
        clear()


def draw(theme: str, styles: list[str]):
    dtheme.apply_official_theme(theme)
    dtheme.allstyles.merge(
        dtheme.ThemeStyles(
            textstyle=TextStyle(font=FontSansSerif.RALEWAYS_REGULAR, size=20),
            shapetextstyle=ShapeTextStyle(font=FontSansSerif.RALEWAYS_REGULAR),
        )
    )

    config(width=100, height=60)
    xs = [10, 30, 50, 70, 90]
    y_text = 8
    y_image = 22
    y_shape = 41
    y_line = 54

    rectangle(
        (60, 0),
        width=20,
        height=60,
        style=ShapeStyle(halign="left", valign="bottom", fcolor=Colors140.LightGray, lwidth=0),
    )
    rectangle(
        (80, 0),
        width=20,
        height=60,
        style=ShapeStyle(halign="left", valign="bottom", fcolor=Colors140.DarkGray, lwidth=0),
    )

    for i, style in enumerate(styles):
        x = xs[i]

        # draw text
        if dtheme.textstyles.has(style):
            if style == "":
                text((x, y_text), "(default)", style=style)
            else:
                text((x, y_text), style, style=style)
            s = style
        else:
            s = style
            s = s.replace("_flat", "")
            s = s.replace("_solid", "")
            s = s.replace("_dashed", "")
            text((x, y_text), style, style=s)
            if i == 1:
                text((x, y_text - 3), "angle=30", style=s)

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
                textstyle=s,
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
                textstyle=s,
            )
            line_bezier1((x - 5, y_line + 2), (x + 5, y_line + 2), (x + 5, y_line - 2), style=style)
        else:
            s = ""
            arrow(
                (x - 9, y_shape),
                (x + 9, y_shape),
                head_width=10,
                head_length=5,
                head_style="<|-|>",
                tail_width=5,
                style=style,
                text="barrow",
                textstyle=s,
            )
            line((x - 5, y_line), (x + 5, y_line), arrowhead="->", width=3)


main()
