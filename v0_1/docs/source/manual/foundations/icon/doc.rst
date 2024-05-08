===============
Drawing Icon
===============

If you're looking to enhance your illustrations with icons, there are several methods you can employ. 
You can utilize the ``image()`` function by providing an icon image file of your choice. 
Alternatively, another option is to utilize ``icon()`` along with ``Icon Modules`` for drawing icons.

Icon Modules
==============

We've curated a selection of icons for your convenience, available in drawlib v0.1.

* ``icon_phosphor``: Derived from Phosphor Icons (https://phosphoricons.com)

Within these modules, each icon is defined as a function, allowing you to choose which icon to draw by calling the respective function. 
Let's explore with examples:

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

Executing this code yields the following image:

.. figure:: image1.png
    :width: 500
    :class: with-border
    :align: center

    image1.png

Similar to other drawing items, the style of icons can be managed using the ``IconStyle`` class.
We use ``IconStyle`` for icon's style.

IconStyle encompasses these attributes

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
    :width: 500
    :class: with-border
    :align: center

    image2.png

icon()
=========

``icon()`` is a versatile function for displaying font icons. 
Internally, icon modules utilize icon().

The function arguments are:

* ``xy``
* ``width``
* ``code``: Font code
* ``file``: Font file
* ``angle``
* ``style``

The arguments xy to file are mandatory, while the latter are optional.
Let's explore its usage with FontAwesome Free:

.. literalinclude:: image3.py
   :language: python
   :linenos:
   :caption: image3.py

Executing this code generates the following image:

.. figure:: image3.png
    :width: 500
    :class: with-border
    :align: center

    image3.png

While FontAwesome is widely recognized, full access necessitates a commercial license. 
The free version may lack variation and style consistency. 
Therefore, we do not currently provide an icon module for it.
