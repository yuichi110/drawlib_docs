from drawlib.apis import *


def draw_square(dpi, color, text_, file):
    clear()
    config(100, 100, dpi, background_color=color)
    text(
        (50, 50),
        text_,
        style=TextStyle(
            color=Colors140.Black,
            halign="center",
            valign="center",
            size=150,
        ),
    )
    save(file)


for dpi, color in [
    (10, Colors.Red),
    (20, Colors.Yellow),
    (30, Colors.Green),
    (40, Colors.Gray),
]:
    draw_square(dpi, color, f"{dpi * 10}\nx\n{dpi * 10}", f"{dpi * 10}px.png")
