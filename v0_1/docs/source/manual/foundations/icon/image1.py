from drawlib.apis import *
from drawlib.apis import dicon_phosphor as ph

config(width=100, dpi=100, grid=True)

ph.address_book(
    (100, 50),
    width=10,
    style=IconStyle(
        color=Colors.Red,
    ),
)

save()
