=================================
Official Theme: default
=================================

Theme ``default`` is default drawlib theme.
It is traditional styling and requires less knowledge to use.

Theme ``simple`` might be better if you want to use many style types such as flat(no-border) and outlined shapes.
The theme color is exactly same to default.

Main Colors
==============

Theme default posses 5 colors.

- ``blue``: light blue. RGB(109, 124, 197)
- ``green``: light green. RGB(112, 194, 191) 
- ``pink``: light pink. RGB(193, 102, 107)
- ``black``: soft black. RGB(27, 38, 59)
- ``white``: white. RGB(255, 255, 255)

Color ``black`` is not real RGB(0, 0, 0) black.
Here is a color chart.

.. figure:: image_colors.png
    :width: 600
    :class: with-border
    :align: center

    image_colors.png

Style Names
==============

Theme default posses 6 style names which includes default(no-name).

- default(no name): black for icon/line/text, blue for shape
- ``blue``: black for shape line. blue for all others.
- ``green``: black for shape line. greeb for all others.
- ``pink``: black for shape line. pink for all others.
- ``black``: white for shape line. black for all.
- ``white``: black for shape line. white for others.

Here is a example of theme styles.
Each drawing items are applied the styles.

- heart: ``icon()``
- line: ``line()``
- rectangle: ``rectangle()``
- python logo: ``image()``
- text: ``text()``

.. figure:: image_style.png
    :width: 600
    :class: with-border
    :align: center

    image_colors.png

You can check which style name supports what style class via ``dtheme.print_style_table()``.

.. literalinclude:: print_style_table.py
   :language: python
   :linenos:
   :caption: style table

Theme ``default`` supports all style class on all style names.