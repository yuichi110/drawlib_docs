========================================
Create Your Custom Theme from Scratch
========================================

We provides official themes.
But some users may want to create your own theme.

You can create your own theme with this procedure.

- Create default theme styles
- Optional: Create named theme styles such as "blue".
- Optional: Define background color and source code font.
- Passing them to ``dtheme.apply_custom_theme()``

Let's take a look

Create Theme Style Object
============================

We use data class ``dtheme.ThemeStyles`` for defining theme styles.
This class is just a holder of drawlib's styles such as ``LineStyle`` and ``ShapeStyle`` etc.
After defining data, binding styles to style name at later.

You need to define themes at least for default styles.
If you want named styles which can be retrieved like ``circle((50, 50), radius=10, style="blue")``, you need to define styles for the each style name.

All members of the this class is optional for ``named_styles``.
But ``default_style`` requires all of belows items.

- iconstyle
- imagestyle
- linestyle
- linearrowstyle
- shapestyle
- shapetextstyle
- textstyle

Other items are optional on default style too.


Apply Theme Styles
====================

``dtheme.apply_custom_theme()`` provides setting custom theme feature.
It takes these arguments.

- default_style: default style.
- named_styles: list of "name and style" pairs.
- theme_colors: list of "name and color" pairs.
- backgroundcolor: background color
- sourcecodefont: source code font

We use ``dtheme.ThemeStyles`` for ``default_style`` and ``named_styles``.
Mandatory arg is only ``default_style``.

OK, let's check create custom theme which uses gold and silver colors.

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

We define theme styles first.
After that, calling ``dtheme.apply_custom_theme()``.

.. figure:: image1.png
    :width: 600
    :class: with-border
    :align: center

    image1.png

You can see your theme is applied.