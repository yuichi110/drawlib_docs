from drawlib.apis import *

config(width=100, height=50)

# before change
text((25, 15), "Hello Drawlib!!")
text((25, 35), "Hello Drawlib!!", style="green")

# change theme style
default_text_style = dtheme.textstyles.get()
default_text_style.size = 24
default_text_style.font = FontSansSerif.RALEWAYS_REGULAR
dtheme.textstyles.set(default_text_style)
green_text_style = dtheme.textstyles.get("green")
green_text_style.size = 24
green_text_style.font = FontSansSerif.RALEWAYS_REGULAR
dtheme.textstyles.set(green_text_style, "green")

# after change
text((75, 15), "Hello Drawlib!!")
text((75, 35), "Hello Drawlib!!", style="green")

save()
