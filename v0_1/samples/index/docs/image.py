from drawlib.apis import *

# Import styles like HTML reference CSS
import docs.style

# Configure drawing canvas size
config(width=100, height=60)

# Use predefined styles
circle(xy=(25, 35), radius=15, style="mystyle")
text(xy=(25, 10), text="Circle", style="mystyle")
rectangle(xy=(75, 35), width=25, height=25, style="mystyle")
text(xy=(75, 10), text="Rectangle", style="mystyle")

# Save canvas
save()
