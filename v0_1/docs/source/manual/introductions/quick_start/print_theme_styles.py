from drawlib.apis import *

dtheme.apply_official_theme("default")
dtheme.print_style_table()

# +----------------+---+-----+-------+------+-------+-------+
# | class \ name   |   | red | green | blue | black | white |
# +----------------+---+-----+-------+------+-------+-------+
# | IconStyle      | x | x   | x     | x    | x     | x     |
# | ImageStyle     | x | x   | x     | x    | x     | x     |
# | LineStyle      | x | x   | x     | x    | x     | x     |
# | LineArrowStyle | x | x   | x     | x    | x     | x     |
# | ShapeStyle     | x | x   | x     | x    | x     | x     |
# | ShapeTextStyle | x | x   | x     | x    | x     | x     |
# | TextStyle      | x | x   | x     | x    | x     | x     |
# +----------------+---+-----+-------+------+-------+-------+

dtheme.apply_official_theme("default2")
dtheme.print_style_table()

# +----------------+---+------+------+------+-------+------------+------------+--------+-------------+-------------+
# | class \ name   |   | thin | bold | flat | solid | solid_thin | solid_bold | dashed | dashed_thin | dashed_bold |
# +----------------+---+------+------+------+-------+------------+------------+--------+-------------+-------------+
# | IconStyle      | x | x    | x    | x    |       |            |            |        |             |             |
# | ImageStyle     | x | x    | x    | x    | x     | x          | x          | x      | x           | x           |
# | LineStyle      | x | x    | x    |      | x     | x          | x          | x      | x           | x           |
# | LineArrowStyle | x | x    | x    |      | x     | x          | x          | x      | x           | x           |
# | ShapeStyle     | x | x    | x    | x    | x     | x          | x          | x      | x           | x           |
# | ShapeTextStyle | x | x    | x    |      |       |            |            |        |             |             |
# | TextStyle      | x | x    | x    |      |       |            |            |        |             |             |
# +----------------+---+------+------+------+-------+------------+------------+--------+-------------+-------------+

# +----------------+-----+----------+----------+----------+-----------+----------------+----------------+------------+-----------------+-----------------+
# | class \ name   | red | red_thin | red_bold | red_flat | red_solid | red_solid_thin | red_solid_bold | red_dashed | red_dashed_thin | red_dashed_bold |
# +----------------+-----+----------+----------+----------+-----------+----------------+----------------+------------+-----------------+-----------------+
# | IconStyle      | x   | x        | x        | x        |           |                |                |            |                 |                 |
# | ImageStyle     | x   | x        | x        | x        | x         | x              | x              | x          | x               | x               |
# | LineStyle      | x   | x        | x        |          | x         | x              | x              | x          | x               | x               |
# | LineArrowStyle | x   | x        | x        |          | x         | x              | x              | x          | x               | x               |
# | ShapeStyle     | x   | x        | x        | x        | x         | x              | x              | x          | x               | x               |
# | ShapeTextStyle | x   | x        | x        |          |           |                |                |            |                 |                 |
# | TextStyle      | x   | x        | x        |          |           |                |                |            |                 |                 |
# +----------------+-----+----------+----------+----------+-----------+----------------+----------------+------------+-----------------+-----------------+

# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+
# | class \ name   | green | green_thin | green_bold | green_flat | green_solid | green_solid_thin | green_solid_bold | green_dashed | green_dashed_thin | green_dashed_bold |
# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+
# | IconStyle      | x     | x          | x          | x          |             |                  |                  |              |                   |                   |
# | ImageStyle     | x     | x          | x          | x          | x           | x                | x                | x            | x                 | x                 |
# | LineStyle      | x     | x          | x          |            | x           | x                | x                | x            | x                 | x                 |
# | LineArrowStyle | x     | x          | x          |            | x           | x                | x                | x            | x                 | x                 |
# | ShapeStyle     | x     | x          | x          | x          | x           | x                | x                | x            | x                 | x                 |
# | ShapeTextStyle | x     | x          | x          |            |             |                  |                  |              |                   |                   |
# | TextStyle      | x     | x          | x          |            |             |                  |                  |              |                   |                   |
# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+

# +----------------+------+-----------+-----------+-----------+------------+-----------------+-----------------+-------------+------------------+------------------+
# | class \ name   | blue | blue_thin | blue_bold | blue_flat | blue_solid | blue_solid_thin | blue_solid_bold | blue_dashed | blue_dashed_thin | blue_dashed_bold |
# +----------------+------+-----------+-----------+-----------+------------+-----------------+-----------------+-------------+------------------+------------------+
# | IconStyle      | x    | x         | x         | x         |            |                 |                 |             |                  |                  |
# | ImageStyle     | x    | x         | x         | x         | x          | x               | x               | x           | x                | x                |
# | LineStyle      | x    | x         | x         |           | x          | x               | x               | x           | x                | x                |
# | LineArrowStyle | x    | x         | x         |           | x          | x               | x               | x           | x                | x                |
# | ShapeStyle     | x    | x         | x         | x         | x          | x               | x               | x           | x                | x                |
# | ShapeTextStyle | x    | x         | x         |           |            |                 |                 |             |                  |                  |
# | TextStyle      | x    | x         | x         |           |            |                 |                 |             |                  |                  |
# +----------------+------+-----------+-----------+-----------+------------+-----------------+-----------------+-------------+------------------+------------------+

# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+
# | class \ name   | black | black_thin | black_bold | black_flat | black_solid | black_solid_thin | black_solid_bold | black_dashed | black_dashed_thin | black_dashed_bold |
# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+
# | IconStyle      | x     | x          | x          | x          |             |                  |                  |              |                   |                   |
# | ImageStyle     | x     | x          | x          | x          | x           | x                | x                | x            | x                 | x                 |
# | LineStyle      | x     | x          | x          |            | x           | x                | x                | x            | x                 | x                 |
# | LineArrowStyle | x     | x          | x          |            | x           | x                | x                | x            | x                 | x                 |
# | ShapeStyle     | x     | x          | x          | x          | x           | x                | x                | x            | x                 | x                 |
# | ShapeTextStyle | x     | x          | x          |            |             |                  |                  |              |                   |                   |
# | TextStyle      | x     | x          | x          |            |             |                  |                  |              |                   |                   |
# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+

# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+
# | class \ name   | white | white_thin | white_bold | white_flat | white_solid | white_solid_thin | white_solid_bold | white_dashed | white_dashed_thin | white_dashed_bold |
# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+
# | IconStyle      | x     | x          | x          | x          |             |                  |                  |              |                   |                   |
# | ImageStyle     | x     | x          | x          | x          | x           | x                | x                | x            | x                 | x                 |
# | LineStyle      | x     | x          | x          |            | x           | x                | x                | x            | x                 | x                 |
# | LineArrowStyle | x     | x          | x          |            | x           | x                | x                | x            | x                 | x                 |
# | ShapeStyle     | x     | x          | x          | x          | x           | x                | x                | x            | x                 | x                 |
# | ShapeTextStyle | x     | x          | x          |            |             |                  |                  |              |                   |                   |
# | TextStyle      | x     | x          | x          |            |             |                  |                  |              |                   |                   |
# +----------------+-------+------------+------------+------------+-------------+------------------+------------------+--------------+-------------------+-------------------+
