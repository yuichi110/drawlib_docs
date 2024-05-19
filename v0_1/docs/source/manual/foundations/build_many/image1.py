from drawlib.apis import *

dexec("./.drawlib")
config(width=100, height=50)
text((50, 15), "Hello Drawlib1", style="gold")
image((50, 35), width=20, image=Dimage.cache.get("python"))
save()
