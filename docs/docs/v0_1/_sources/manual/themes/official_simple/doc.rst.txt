=========================
Official Theme: simple
=========================

Theme ``simple`` is enhancement of default theme ``default``.
Theme ``default`` has only 1 style per color.
But theme ``simple`` posess 4 styler per color.

Colors
==============

Theme default posses 5 colors.

- ``blue``: light blue (main)
- ``green``: light green
- ``pink``: light pink
- ``black``: soft black
- ``white``: white

.. figure:: image_colors.png
    :width: 600
    :class: with-border
    :align: center

    image_colors.png

Style Types
===============

Each color posses these styles.

- default: Having border and fill color
- ``flat`` style: Having no border. (white color actually)
- ``solid`` style: Shape has outline but no fill.
- ``dashed`` style: Dashed line, Dashed outline.

Let's take a look at blue example.

.. figure:: image_styles_blue.png
    :width: 600
    :class: with-border
    :align: center

Please be careful, drawlib try to avoid having overlapped style.
For example LineStyle of ``blue_solid`` doesn't exist.
Since it is covered on LineStyle ``blue``.

Flat looks like no border.
However it has white color (same to background) border.
It is not visible normally, and useful when you stuck the shapes.

Bottom side is default flat style.
Top side updated flat style with deleteing white color border.

.. figure:: image_flat.png
    :width: 600
    :class: with-border
    :align: center

Here is how to change border.
You can check details at customizing official style documentation.

.. literalinclude:: image_flat.py
   :language: python
   :linenos:
   :caption: style table

Change Line Width
===================

Changing line width might be popular modification for some of you.
We recommend to add new style name for standadize line width between images.
However you can modify it on the spot with ``<style-name>.<line-width-percentage>`` syntax.
For example, ``blue_solid.50`` makes half width line and ``blue_solid.200`` makes double.

Here is a example.

.. figure:: image_linewidth.png
    :width: 600
    :class: with-border
    :align: center

You can specify only int value after dot.
``blue_solid`` and ``blue_solid.100`` are same since 100% is original width.


Style Names
==============

Here is a list of style names.

.. literalinclude:: print_style_table.py
   :language: python
   :linenos:
   :caption: style table

And output of each styles.

.. figure:: image_style.png
    :width: 600
    :class: with-border
    :align: center

style ``blue``.

.. figure:: image_style_blue.png
    :width: 600
    :class: with-border
    :align: center

style ``green``.

.. figure:: image_style_green.png
    :width: 600
    :class: with-border
    :align: center

style ``pink``.

.. figure:: image_style_pink.png
    :width: 600
    :class: with-border
    :align: center

style ``black``.

.. figure:: image_style_black.png
    :width: 600
    :class: with-border
    :align: center

black's shape has line color white.

style ``white``.

.. figure:: image_style_white.png
    :width: 600
    :class: with-border
    :align: center
