from drawlib.apis import *

config(width=100, height=50, grid_only=True)
arrow((5, 25), (45, 25), tail_width=10, head_width=20, head_length=10)
arrow(
    (75, 5),
    (75, 45),
    tail_width=10,
    head_width=20,
    head_length=10,
    head_style="<|-|>",
    text="arrow()",
)
save()
