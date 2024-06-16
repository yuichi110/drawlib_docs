from drawlib.apis import *

config(width=100, height=50)

# get default style.
default_style = dtheme.linestyles.get()
line((10, 10), (40, 40), arrowhead="->", style=default_style)

# get named style
tstyle = dtheme.textstyles.get("blue")
tstyle.size = 24
tstyle.font = FontSansSerif.RALEWAYS_REGULAR
text((75, 15), "Hello Drawlib!!", style=tstyle)

# update theme style
dtheme.textstyles.set(style=tstyle, name="blue")
text((75, 35), "Theme Style Updated!!", style=dtheme.textstyles.get("blue"))

save()
dtheme.apply_official_theme("default")
