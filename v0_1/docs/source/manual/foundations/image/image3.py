from drawlib.apis import *
import PIL.Image

config(width=100, height=50, grid_only=True)

image(xy=(20, 25), width=20, image="python-logo-notext.png")

dimage = Dimage("python-logo-notext.png")
image(xy=(50, 25), width=20, image=dimage)

file_path = dutil_script.get_relative_path("python-logo-notext.png")
pil_image = PIL.Image.open(file_path)
image(xy=(80, 25), width=20, image=pil_image)

save()
