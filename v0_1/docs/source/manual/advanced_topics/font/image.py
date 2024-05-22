from drawlib.apis import *

height = 50


def draw(text_, font_matrix, file_name):
    clear()
    config(width=100, height=height)
    style1 = TextStyle(size=16)
    style2 = TextStyle(size=13)
    y_pitch = height / (len(font_matrix) + 2)

    for i, fonts in enumerate(font_matrix, start=1):
        name, light, regular, bold = fonts

        y = y_pitch * i
        text((15, y), name, style=style2)

        style_light = style1.copy()
        style_light.font = light
        text((40, y), text=text_, style=style_light)

        style_regular = style1.copy()
        style_regular.font = regular
        text((60, y), text=text_, style=style_regular)

        style_bold = style1.copy()
        style_bold.font = bold
        text((80, y), text=text_, style=style_bold)

    y = y_pitch * (len(font_matrix) + 1)
    text((40, y), "light", style=style2)
    text((60, y), "regular", style=style2)
    text((80, y), "bold", style=style2)

    save(file_name)


draw(
    "Hello Drawlib!",
    [
        ("Font.SANSSERIF", Font.SANSSERIF_LIGHT, Font.SANSSERIF_REGULAR, Font.SANSSERIF_BOLD),
        ("Font.SERIF", Font.SERIF_LIGHT, Font.SERIF_REGULAR, Font.SERIF_BOLD),
    ],
    "image_Font.png",
)

draw(
    "Hello Drawlib!",
    [
        ("FontSanSerif.LATO", FontSanSerif.LATO_LIGHT, FontSanSerif.LATO_REGULAR, FontSanSerif.LATO_BOLD),
        (
            "FontSanSerif.MONTSERRAT",
            FontSanSerif.MONTSERRAT_LIGHT,
            FontSanSerif.MONTSERRAT_REGULAR,
            FontSanSerif.MONTSERRAT_BOLD,
        ),
        ("FontSanSerif.OSWALD", FontSanSerif.OSWALD_LIGHT, FontSanSerif.OSWALD_REGULAR, FontSanSerif.OSWALD_BOLD),
        ("FontSanSerif.POPPINS", FontSanSerif.POPPINS_LIGHT, FontSanSerif.POPPINS_REGULAR, FontSanSerif.POPPINS_BOLD),
        (
            "FontSanSerif.RALEWAYS",
            FontSanSerif.RALEWAYS_LIGHT,
            FontSanSerif.RALEWAYS_REGULAR,
            FontSanSerif.RALEWAYS_BOLD,
        ),
    ],
    "image_FontSanSerif.png",
)
