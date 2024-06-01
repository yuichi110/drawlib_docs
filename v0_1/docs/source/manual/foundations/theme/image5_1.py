from drawlib.apis import *

dtheme.apply_official_theme("default")
dtheme.allstyles.rename("blue", "1")
dtheme.allstyles.rename("green", "2")
dtheme.allstyles.rename("pink", "3")

config(width=100, height=50)
circle((20, 25), radius=10, style="1")
rectangle((50, 25), width=20, height=20, style="2")
tstyle = dtheme.textstyles.get("3")
tstyle.size = 28
text((80, 25), text="Hello\nDrawlib!", style=tstyle)
save()
