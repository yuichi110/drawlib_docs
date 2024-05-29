from drawlib.apis import *

default = dtheme.ThemeStyle(
    backgroundcolor=Colors140.AliceBlue,
    sourcecodefont=FontSourceCode.ROBOTO_MONO,
    iconstyle=IconStyle(style="fill", color=Colors140.Gold),
    imagestyle=ImageStyle(lcolor=Colors140.Gold, lwidth=0),
    linestyle=LineStyle(width=3, color=Colors140.Gold),
    linearrowstyle=LineArrowStyle(lwidth=3, color=Colors140.Gold),
    shapestyle=ShapeStyle(lwidth=0, lcolor=Colors140.Black, fcolor=Colors140.Gold),
    shapetextstyle=ShapeTextStyle(color=Colors140.DarkRed, font=FontSansSerif.RALEWAYS_BOLD),
    textstyle=TextStyle(color=Colors140.DarkRed, font=FontSansSerif.RALEWAYS_BOLD),
)

gold = dtheme.ThemeStyle(
    iconstyle=IconStyle(style="fill", color=Colors140.Gold),
    imagestyle=ImageStyle(lcolor=Colors140.Gold, lwidth=0),
    linestyle=LineStyle(width=3, color=Colors140.Gold),
    linearrowstyle=LineArrowStyle(lwidth=3, color=Colors140.Gold),
    shapestyle=ShapeStyle(lwidth=0, lcolor=Colors140.Black, fcolor=Colors140.Gold),
    shapetextstyle=ShapeTextStyle(color=Colors140.Gold, font=FontSansSerif.RALEWAYS_BOLD),
    textstyle=TextStyle(color=Colors140.Gold, font=FontSansSerif.RALEWAYS_BOLD),
)

silver = dtheme.ThemeStyle(
    iconstyle=IconStyle(style="fill", color=Colors140.Silver),
    imagestyle=ImageStyle(lcolor=Colors140.Silver, lwidth=0),
    linestyle=LineStyle(width=3, color=Colors140.Silver),
    linearrowstyle=LineArrowStyle(lwidth=3, color=Colors140.Silver),
    shapestyle=ShapeStyle(lwidth=0, lcolor=Colors140.Black, fcolor=Colors140.Silver),
    shapetextstyle=ShapeTextStyle(color=Colors140.Silver, font=FontSansSerif.RALEWAYS_BOLD),
    textstyle=TextStyle(color=Colors140.Silver, font=FontSansSerif.RALEWAYS_BOLD),
)

dtheme.apply_custom_theme(
    default_style=default,
    named_styles=[
        ("gold", gold),
        ("silver", silver),
    ],
    theme_colors=[
        ("gold", Colors140.Gold),
        ("silver", Colors140.Silver),
    ],
)

config(width=100, height=50)
x1 = 20
x2 = 50
x3 = 80
y1 = 10
y2 = 25
y3 = 40

line((x1 - 10, y1), (x1 + 10, y1))
circle((x1, y2), radius=10)
text((x1, y3), "Hello Drawlib!")

for x, name in [(x2, "gold"), (x3, "silver")]:
    line((x - 10, y1), (x + 10, y1), style=name)
    circle((x, y2), radius=10, style=name)
    text((x, y3), "Hello Drawlib!", style=name)

save()
clear(initialize_theme=True)
