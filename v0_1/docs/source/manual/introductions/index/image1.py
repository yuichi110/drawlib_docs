from drawlib.apis import *

config(grid=True, height=60)

CODE = """from drawlib.apis import *

circle(
    xy=(50, 50),
    radius=30,
    style=ShapeStyle(
        lstyle="dashed",
        lcolor=Colors140.BlueViolet,
        lwidth=5,
        fcolor=Colors140.Turquoise,
    ),
)
save()"""


def upper():
    y = 50
    text(
        xy=(20, y),
        text="Drawlib",
        style=TextStyle(size=28, font=FontRoboto.ROBOTO_BOLD),
    )
    dicon_phosphor.heart(
        xy=(40, y),
        width=10,
        style=IconStyle(color=Colors140.Pink, style="fill"),
    )
    text(
        xy=(70, y),
        text="Illustration as Code",
        style=TextStyle(size=28, font=FontRoboto.ROBOTO_BOLD),
    )


def middle():
    y = 13
    style = ImageStyle(lwidth=1, valign="bottom")
    sc = dsart.SourceCode(style="default", font=FontSourceCode.ROBOTO_MONO)
    sc.draw((22, y), width=32, code=CODE, style=style)
    arrow((45, 24), (55, 24), tail_width=5, head_width=10, head_length=5, head_style="-|>")
    image((77, y), width=25, image="inside.png", style=style)


def lower():
    y = 7
    style = TextStyle(size=20, font=FontRoboto.ROBOTO_REGULAR)
    dicon_phosphor.file_py(xy=(13, y), width=5)
    text((26, y), "Python Code", style=style)
    text((50, y), "to", style=style)
    dicon_phosphor.file_image(xy=(69, y), width=5)
    text((80, y), "Illustration", style=style)


upper()
middle()
lower()

save()
