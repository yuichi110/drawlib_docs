from drawlib.apis import *

config(grid=True, height=60)

rect_width = 20
rect_height = 38
ls = LineStyle(width=0.5)
ts = TextStyle(size=12)


def left():
    text((15, 54), "Drawlib's\nDocument Source")

    rectangle(
        xy=(15, 30),
        width=rect_width,
        height=rect_height,
        r=2,
        style=ShapeStyle(fcolor=Colors.Transparent, lstyle="dashed"),
    )

    x = 8
    icon_phosphor.folder((x, 45), width=3)
    text((x + 6, 45), "docs", style=ts)
    line((x, 43), (x, 13), style=ls)

    line((x, 42), (x + 1, 42), style=ls)
    icon_phosphor.folder((x + 3, 42), width=3)
    text((x + 9, 42), "commons", style=TextStyle(size=12))
    line((x + 3, 40), (x + 3, 35), style=LineStyle(width=0.5))
    icon_phosphor.file_py((x + 6, 39), width=3, style=IconStyle(color=Colors.Red))
    text((x + 12, 39), "style.py", style=TextStyle(size=12, color=Colors.Red))
    line((x + 3, 39), (x + 4, 39), style=LineStyle(width=0.5))
    icon_phosphor.file_py((x + 6, 36), width=3, style=IconStyle(color=Colors.Red))
    text((x + 12, 36), "util.py", style=TextStyle(size=12, color=Colors.Red))
    line((x + 3, 36), (x + 4, 36), style=LineStyle(width=0.5))

    line((x, 30), (x + 1, 30), style=ls)
    icon_phosphor.folder((x + 3, 30), width=3)
    text((x + 9, 30), "chapter1", style=TextStyle(size=12))
    line((x + 3, 28), (x + 3, 19), style=LineStyle(width=0.5))
    icon_phosphor.file_md((x + 6, 27), width=3)
    text((x + 12, 27), "doc.md", style=TextStyle(size=12))
    line((x + 3, 27), (x + 4, 27), style=LineStyle(width=0.5))
    icon_phosphor.file_py((x + 6, 24), width=3, style=IconStyle(color=Colors.Red))
    text((x + 12, 24), "img1.py", style=TextStyle(size=12, color=Colors.Red))
    line((x + 3, 24), (x + 4, 24), style=LineStyle(width=0.5))
    icon_phosphor.file_py((x + 6, 21), width=3, style=IconStyle(color=Colors.Red))
    text((x + 12, 21), "img2.py", style=TextStyle(size=12, color=Colors.Red))
    line((x + 3, 21), (x + 4, 21), style=LineStyle(width=0.5))

    line((x, 15), (x + 1, 15), style=ls)
    icon_phosphor.folder((x + 3, 15), width=3)
    text((x + 9, 15), "chapter2", style=TextStyle(size=12))


def center():
    text((50, 54), "Traditional\nDocument Source")
    rectangle(
        xy=(50, 30),
        width=rect_width,
        height=rect_height,
        r=2,
        style=ShapeStyle(fcolor=Colors.Transparent, lstyle="dashed"),
    )

    x = 43
    icon_phosphor.folder((x, 45), width=3)
    text((x + 6, 45), "docs", style=ts)
    line((x, 43), (x, 13), style=ls)

    line((x, 30), (x + 1, 30), style=ls)
    icon_phosphor.folder((x + 3, 30), width=3)
    text((x + 9, 30), "chapter1", style=TextStyle(size=12))
    line((x + 3, 28), (x + 3, 19), style=LineStyle(width=0.5))
    icon_phosphor.file_md((x + 6, 27), width=3)
    text((x + 12, 27), "doc.md", style=TextStyle(size=12))
    line((x + 3, 27), (x + 4, 27), style=LineStyle(width=0.5))
    icon_phosphor.file_image((x + 6, 24), width=3, style=IconStyle(color=Colors.Red))
    text((x + 12, 24), "img1.png", style=TextStyle(size=12, color=Colors.Red))
    line((x + 3, 24), (x + 4, 24), style=LineStyle(width=0.5))
    icon_phosphor.file_image((x + 6, 21), width=3, style=IconStyle(color=Colors.Red))
    text((x + 12, 21), "img2.png", style=TextStyle(size=12, color=Colors.Red))
    line((x + 3, 21), (x + 4, 21), style=LineStyle(width=0.5))

    line((x, 15), (x + 1, 15), style=ls)
    icon_phosphor.folder((x + 3, 15), width=3)
    text((x + 9, 15), "chapter2", style=TextStyle(size=12))


def right():
    text((85, 54), "Output Documents")

    rectangle(
        xy=(85, 30),
        width=rect_width,
        height=rect_height,
        r=2,
        style=ShapeStyle(fcolor=Colors.Transparent, lstyle="dashed"),
    )

    icon_phosphor.file_pdf((85, 43), width=6)
    icon_phosphor.file_html((85, 35), width=6)
    icon_phosphor.file_ppt((85, 27), width=6)
    icon_phosphor.book_bookmark((85, 19), width=6)
    text((85, 14.5), text="eBook")


def bottom():
    rectangle(
        xy=(50, 5),
        width=90,
        height=6,
        r=2,
        style=ShapeStyle(fcolor=Colors.Transparent),
    )
    icon_phosphor.github_logo((17, 5), width=5)
    text((53, 5), "Illustration and doc text versioning with CI/CD automation")


left()
arrow(
    (28, 35),
    (37, 35),
    tail_width=3,
    head_width=6,
    head_length=3,
    style=ShapeStyle(lcolor=Colors.Red, fcolor=Colors.Red),
    text="Drawlib",
    textstyle=ShapeTextStyle(
        size=14,
        color=Colors.White,
        font=FontRoboto.ROBOTO_BOLD,
        xy_shift=(-0.5, -0.1),
    ),
)
text((32, 25), "Build\nImages", style=TextStyle(color=Colors.Red))
center()
arrow(
    (63, 35),
    (72, 35),
    tail_width=3,
    head_width=6,
    head_length=3,
    style=ShapeStyle(fcolor=Colors.White),
)
text((67, 25), "Build\nDocs")
right()
bottom()
save()
