======================
Line and Arrow Style
======================

All functions which draw line takes style option as argument.
We supports these 2 style class.

* LineStyle
* LineArrowStyle

As there name shows, LineStyle is used for drawing line.
And LineArowStyle is used for drawing line which has arrow head.

We have function ``arrow()`` too.
But it is thick and bold arrow shape. Not an arrow line.

LineStyle
===========

LineStyle has these attributes.

* width: Line width. float value
* color: Line color. RGB (0~255, 0~255, 0~255) or RGBA (0~255, 0~255, 0~255, 0~1.0). You can use Color class
* alpha: Line alpha. 0.0 ~ 1.0. 0 is totally transparent
* style: Line style, such as solid, dash etc

Let's check by examples.

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

We change style 1 by 1.
But you can change style at same time such as ``LineStyle(color=Colors.Red, width=5, style="dashed")``.

.. figure:: image1.png
    :width: 500
    :class: with-border
    :align: center

    image1.png

You can see line styles


LineArrowStyle
=================

``LineArrowStyle`` is almost similar to ``LineStyle``.
But it has few additional attributed and having change of original attribute.
It has these attributes.

* lwidth: Line width
* lstyle: Line style
* hstyle: Arrow head style
* hscale: Arrow head scale (size)
* color: Arrow line color
* alpha: Arrow line alpha

To distinguish whether line and arrow head parameter, few attribute starts from ``l(line)`` and others starts from ``h(head)``.
``hstyle`` can have these values.

* ``"->:``: Arrow at end point. 
* ``"<-:``: Arrow at start point. 
* ``"<->:``: Arrow at both start and end point. 
* ``"-|>:``: Filled arrow at end point. 
* ``"<|-:``: Filled arrow at start point. 
* ``"<|-|>:``: Filled arrow at both start and end point. 

Let's check by example.

.. literalinclude:: image2.py
   :language: python
   :linenos:
   :caption: image2.py

We change style 1 by 1.
But you can change style at same time such as ``LineArrowStyle(color=Colors.Red, lwidth=5, lstyle="dashed", hstyle="<->")``.

.. figure:: image2.png
    :width: 500
    :class: with-border
    :align: center

    image2.png

To draw default arrow line, please pass ``LineArrowStyle()`` to line.
If you don't specify style, normal line will be drawn.