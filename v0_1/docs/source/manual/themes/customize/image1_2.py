from drawlib.apis import *

config(width=100, height=50)

# before change
text((25, 15), "Hello Drawlib!!")
text((25, 35), "Hello Drawlib!!", style="green")

# change all theme text styles
for name in dtheme.textstyles.list():
    text_style = dtheme.textstyles.get(name)
    text_style.size = 24
    text_style.font = FontSansSerif.RALEWAYS_REGULAR
    dtheme.textstyles.set(text_style, name)

# after change
text((75, 15), "Hello Drawlib!!")
text((75, 35), "Hello Drawlib!!", style="green")

save()
dtheme.apply_official_theme("default")
