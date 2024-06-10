from drawlib.apis import *

dtheme.apply_official_theme("essentials")
config(width=100, height=50)
line_y = 40
text_y = 10

# default style
line((8, line_y), (22, line_y))
circle((15, 25), radius=8)
text((15, text_y), text="no style")

# blue style
line((31, line_y), (45, line_y), style="lightblue")
circle((38, 25), radius=8, style="lightblue")
text((38, text_y), text='style="lightblue"', style="lightblue")

# green style
line((55, line_y), (69, line_y), style="lightgreen")
circle((62, 25), radius=8, style="lightgreen")
text((62, text_y), text='style="lightgreen"', style="lightgreen")

# pink style
line((78, line_y), (92, line_y), style="lightred")
circle((85, 25), radius=8, style="lightred")
text((85, text_y), text='style="lightred"', style="lightred")

dtheme.print_style_table()
# +----------------+---+-----------+-----------+---------+-----------+-------------+-------------+----------+----------+-------------+---------------+------------+--------+--------+---------+----------+-------------+--------+--------+----------+----------+
# |                |   | turquoise | green_sea | emerald | nephritis | peter_river | belize_hole | amethyst | wisteria | wet_asphalt | midnight_blue | sun_flower | orange | carrot | pumpkin | alizarin | pomegranate | clouds | silver | concrete | asbestos |
# +----------------+---+-----------+-----------+---------+-----------+-------------+-------------+----------+----------+-------------+---------------+------------+--------+--------+---------+----------+-------------+--------+--------+----------+----------+
# | IconStyle      | x | x         | x         | x       | x         | x           | x           | x        | x        | x           | x             | x          | x      | x      | x       | x        | x           | x      | x      | x        | x        |
# | ImageStyle     | x | x         | x         | x       | x         | x           | x           | x        | x        | x           | x             | x          | x      | x      | x       | x        | x           | x      | x      | x        | x        |
# | LineStyle      | x | x         | x         | x       | x         | x           | x           | x        | x        | x           | x             | x          | x      | x      | x       | x        | x           | x      | x      | x        | x        |
# | LineArrowStyle | x | x         | x         | x       | x         | x           | x           | x        | x        | x           | x             | x          | x      | x      | x       | x        | x           | x      | x      | x        | x        |
# | ShapeStyle     | x | x         | x         | x       | x         | x           | x           | x        | x        | x           | x             | x          | x      | x      | x       | x        | x           | x      | x      | x        | x        |
# | ShapeTextStyle | x | x         | x         | x       | x         | x           | x           | x        | x        | x           | x             | x          | x      | x      | x       | x        | x           | x      | x      | x        | x        |
# | TextStyle      | x | x         | x         | x       | x         | x           | x           | x        | x        | x           | x             | x          | x      | x      | x       | x        | x           | x      | x      | x        | x        |
# +----------------+---+-----------+-----------+---------+-----------+-------------+-------------+----------+----------+-------------+---------------+------------+--------+--------+---------+----------+-------------+--------+--------+----------+----------+

save()
