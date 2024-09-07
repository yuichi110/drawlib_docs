from drawlib.apis import *

config(width=100, height=50, grid=True)

gl1 = dsart.GridLayout(num_column=7, num_row=3)
gl1.add(position=(0, 0), width=5, height=1, text="Host OS")
gl1.add(position=(0, 1), width=5, height=1, text="Python")
gl1.add(position=(0, 2), width=1, height=1, text="D")
gl1.add(position=(1, 2), width=1, height=1, text="r")
gl1.add(position=(2, 2), width=1, height=1, text="a")
gl1.add(position=(3, 2), width=1, height=1, text="w")
gl1.add(position=(4, 2), width=1, height=1, text="l")
gl1.add(position=(5, 2), width=1, height=1, text="i")
gl1.add(position=(6, 2), width=1, height=1, text="b")
gl1.draw((5, 10), width=40, height=20, margin=1)
text((25, 5), text="Grid Layout: Column 7, Row 3.")

gl2 = dsart.GridLayout(num_column=7, num_row=3, default_r=1, default_style="solid")
gl2.add(position=(0, 0), width=7, height=1, text="Host OS", style="blue", textstyle="white", text_xy_shift=(10, 0))
gl2.add(position=(0, 1), width=7, height=1, text="Python", style="green", textstyle="white", text_xy_shift=(-10, 0))
gl2.add(position=(0, 2), width=1, height=1, text="D")
gl2.add(position=(1, 2), width=1, height=1, text="r")
gl2.add(position=(2, 2), width=1, height=1, text="a", textangle=90)
gl2.add(position=(3, 2), width=1, height=1, text="w", textangle=180)
gl2.add(position=(4, 2), width=1, height=1, text="l", textangle=270)
gl2.add(position=(5, 2), width=1, height=1, text="i")
gl2.add(position=(6, 2), width=1, height=1, text="b")
gl2.draw((55, 10), width=40, height=20, margin=1, outer_style="solid", outer_r=1)

save()
