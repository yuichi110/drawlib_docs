from drawlib.apis import *

config(width=100, height=60)

text((50, 10), "Hello drawlib. こんにちは。")
text(
    (50, 20),
    "Hello drawlib. こんにちは。",
    angle=10,
    style=TextStyle(font=Font.ROBOTO_REGULAR),
)
text(
    (50, 30),
    "Hello drawlib.",
    style=TextStyle(font=FontFile("avenger/regular.ttf")),
)
text(
    (50, 40),
    "Hello drawlib. こんにちは。",
    style=TextStyle(color=Colors.Red, size=24),
)
text(
    (50, 50),
    "Hello drawlib. こんにちは。",
    style=TextStyle(color=Colors.White, bgfcolor=Colors.Black),
)
save()
