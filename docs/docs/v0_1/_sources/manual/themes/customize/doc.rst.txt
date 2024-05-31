===========================
Customize official theme
===========================

You can create your own theme from scratch.
But if you don't need huge modification from official themes, customization might be good.

Update style objects
=====================

You can access to theme style objects through ``dtheme.<type>styles``.
Where the ``<type>`` is equivalent to Style class name.
For example, ``IconStyle`` can be accessed with ``dtheme.iconstyles``.

Each objects posses these methods.

- ``has(name)``: whether the name style exists or not
- ``list()``: get names of styles
- ``get(name)``: get style object
- ``set(name)``: set style object
- ``delete(name)``: delete style object

Here is a update procedure.

1. Get original object. Such as  ``textstyle = dtheme.textstyles.get(name)``
2. Modify style. Such as ``textstyle.size = 24``
3. Repeat modification
4. Set modified object. Such as ``dtheme.textstyles.set(textstyle, name)``

Let's take a look simple example which change text style.

.. literalinclude:: image1_1.py
   :language: python
   :linenos:
   :caption: image1_1.py

.. figure:: image1_1.png
    :width: 600
    :class: with-border
    :align: center

    image1_1.png

You can update style one by one.
However, using ``dtheme.<type>styles.list()`` and for loop is useful for changing all styles with same update.

.. literalinclude:: image1_2.py
   :language: python
   :linenos:
   :caption: image1_2.py

.. figure:: image1_2.png
    :width: 600
    :class: with-border
    :align: center

    image1_2.png


Copy style name
=================

Rename style name
===================