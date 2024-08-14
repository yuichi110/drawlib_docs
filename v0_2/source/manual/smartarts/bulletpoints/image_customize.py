from drawlib.apis import *

config(width=100, height=50, grid=True)


bp = dsart.BulletPoints(
    vertical_margin=4,
    indent_width=4,
    default_style=dtheme.textstyles.get().merge(TextStyle(font=FontSansSerif.RALEWAYS_REGULAR)),
)
bp.set_bullet_style(1, rectangle, "black_solid", args={"width": 1, "height": 1})
bp.set_bullet_style(2, rectangle, "black_flat", args={"width": 1, "height": 1})

bp.add("Type of Drawlib shapes")
bp.set_indent(1)
bp.add(
    "Circle Like Shapes",
    style=dtheme.textstyles.get().merge(
        TextStyle(
            font=FontSansSerif.RALEWAYS_BOLD,
            color=Colors.Red,
        )
    ),
)
bp.set_indent(2)
bp.add("Circle")
bp.add("Start etc.")
bp.set_indent(1)
bp.add(
    "Rectangle Like Shapes",
    style=dtheme.textstyles.get().merge(
        TextStyle(
            font=FontSansSerif.RALEWAYS_BOLD,
            color=Colors.Blue,
        )
    ),
)
bp.set_indent(2)
bp.add("Rectangle")
bp.add("Ellipse etc.")
bp.draw(xy=(60, 40))

save()
