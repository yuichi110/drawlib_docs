from drawlib.apis import *

config(width=100, height=50)

# get default style.
lastyle = dtheme.linearrowstyles.get()
line((10, 10), (40, 40), style=lastyle)

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
