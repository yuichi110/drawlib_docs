from drawlib.apis import *

dtheme.apply_official_theme("rich")
config(width=100, height=50)
line_y = 40
text_y = 10

# default style
line((8, line_y), (22, line_y))
circle((15, 25), radius=8)
text((15, text_y), text="no style")

# blue style
line((31, line_y), (45, line_y), style="belize_hole")
circle((38, 25), radius=8, style="belize_hole")
text((38, text_y), text='style="belize_hole"', style="belize_hole")

# green style
line((55, line_y), (69, line_y), style="green_sea")
circle((62, 25), radius=8, style="green_sea")
text((62, text_y), text='style="green_sea"', style="green_sea")

# pink style
line((78, line_y), (92, line_y), style="pomegranate")
circle((85, 25), radius=8, style="pomegranate")
text((85, text_y), text='style="pomegranate"', style="pomegranate")

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
dtheme.apply_official_theme("default")
