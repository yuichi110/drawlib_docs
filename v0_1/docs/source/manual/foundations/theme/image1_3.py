from drawlib.apis import *

config(width=100, height=50)
text_y = 10
circle((20, 25), radius=8)
text((20, text_y), text="no style")
circle((40, 25), radius=8, style="blue")
text((40, text_y), text='style="blue"')
circle((60, 25), radius=8, style="green")
text((60, text_y), text='style="green"')
circle((80, 25), radius=8, style="pink")
text((80, text_y), text='style="pink"')
save()
