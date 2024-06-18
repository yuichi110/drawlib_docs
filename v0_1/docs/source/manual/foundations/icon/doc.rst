===============
Drawing Icons
===============

If you're looking to enhance your illustrations with icons, drawlib offers several methods to achieve this. 
You can utilize the ``image()`` function by providing an icon image file of your choice. 
Alternatively, you can use ``icon()`` along with dedicated ``Icon Modules`` for drawing icons directly.

Icon Modules
==============

We've curated a selection of icons for your convenience, available in drawlib now.

* ``icon_phosphor``: Derived from Phosphor Icons (https://phosphoricons.com)

Each icon within these modules is defined as a function, allowing you to draw specific icons by simply calling their respective function. 
Let's explore with examples:

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

All functions have these args.

- ``xy`` : coordinate
- ``width`` : icon width
- ``angle`` : angle 0.0~360.0
- ``style`` : Accepts string style name or ``IconStyle`` object.

Executing this code yields the following image:

.. figure:: image1.png
    :width: 600
    :class: with-border
    :align: center

    image1.png

You see lots of variation of only airplane.
``icon_phosphor`` has around 1500 icons.
Similar to other drawing elements, the appearance of icons can be customized using the ``IconStyle`` class, which allows you to control:

``IconStyle`` encompasses these attributes

* ``halign``: Horizontal alignment
* ``valign``: Vertical alignment
* ``style``: Icon style, Supports ``"thin"``, ``"light"``, ``"regular"``, ``"bold"``, or ``"fill"``. The availability of styles depends on the icon modules.
* ``color``: Icon color, specified in RGB (0255, 0255, 0255) or RGBA (0255, 0255, 0255, 0.0~1.0). You can utilize helpers like ``Colors`` and ``Colors140``.
* ``alpha``: Icon transparency, ranging from 0.0 to 1.0, where 0.0 represents total transparency.

Let's illustrate this with an example:

.. literalinclude:: image2.py
   :language: python
   :linenos:
   :caption: image2.py

Executing this code generates the following image:

.. figure:: image2.png
    :width: 600
    :class: with-border
    :align: center

    icon with IconStyle.

You can use theme's pre-defined styles too.

.. literalinclude:: image3.py
   :language: python
   :linenos:
   :caption: image3.py

Icon supports the following styles exclusively:

- thickness of icon: ``thin`` and ``bold``
- fill color: ``flat``
- color of icon

Line style solid and dashed are not supported.

.. figure:: image3.png
    :width: 600
    :class: with-border
    :align: center

    icon with theme's style



icon()
=========

``icon()`` is a versatile function for displaying font icons. 
Internally, icon modules utilize icon().

The function arguments are:

* ``xy``: Coordinates for positioning the icon.
* ``width``: Width of the icon.
* ``code``: Font code representing the icon.
* ``file``: Font file used for rendering the icon.
* ``angle``: Angle for rotating the icon (optional).
* ``style``: Additional style configurations (optional).
.
Let's explore its usage with FontAwesome Free:

.. literalinclude:: image4.py
   :language: python
   :linenos:
   :caption: image4.py

Executing this code generates the following image:

.. figure:: image4.png
    :width: 600
    :class: with-border
    :align: center

    FontAwesome-Free icons

While FontAwesome is widely recognized, its full usage requires a commercial license. 
The free version may lack variation and style consistency. 
Therefore, drawlib does not currently provide an icon module for it.
