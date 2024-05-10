===============
Drawing Shape
===============

Drawlib posses lots of drawing shape functions.
The most basic ones are drawing circle, rectangles etc.
The most minor shapes are bubblespeech, chevron etc.

All of functions are categorized to these 3 types.

* Circle like shape: Specify xy and radius
* Rectangle like shape: Specify xy and width/height
* Other shapes: Arrow(from xy1 to xy2), Polygon(connects xys and fill) etc.

Functions which draw circle like shapes are

* ``circle()``
* ``donuts()``
* ``fan()``
* ``regularpolygon()``
* ``star()``
* ``wedge()``

Functions which draw rectangle like shapes are

* ``arc()``
* ``bubblespeech()``
* ``chevron()``
* ``ellipse()``
* ``parallelogram()``
* ``rectangle()``
* ``rhombus()``
* ``trapezoid()``
* ``triangle``

And last functions which draw other type shapes are

* ``arrow()``
* ``polygon()``
* ``shape()``

Let's take a look all of them except ``shape()`` which we mention at another page by categories.
``shape()`` is useful for drawing shape which is your original.

All of their alignment is horizontally center and vertically center by default.
Which can be changed via style ``ShapeStyle()``.
However ``arrow()`` and ``polygon()`` don't have alignment.
They will ignore alignment attributes.
We will mention styling ``ShapeStyle`` and ``ShapeTextStyle`` in another page.


Draw Circle Like Shapes
=========================

Circle like object specifies xy and radius and other shape specific args.

circle()
---------

Function ``circle()`` draws circle.
Which takes these arguments.

* xy (tuple[float, float]): X, Y coordinate
* radius (float): radius
* angle (float): angle which effects to text
* style (ShapeStyle)
* text (str): center text
* textstyle (ShapeTextStyle)

Let's explore two examples.

.. literalinclude:: image_circle1.py
   :language: python
   :linenos:
   :caption: image_circle1.py

Circle shape doesn't have effect of angle.
However, text has effect.

.. figure:: image_circle1.png
    :width: 500
    :class: with-border
    :align: center

    image_circle1.png

donuts()
---------

Function ``donuts()`` draws donuts like shape.
We specify external radius and width of fill area from external radius.
In another word, internal radius becomes "external radius - width".

This function takes these arguments.

* xy (tuple[float, float]): X, Y coordinate
* radius (float): external radius
* width (float): width of donuts fill area
* angle (float): angle which effects to text
* style (ShapeStyle)
* text (str): center text
* textstyle (ShapeTextStyle)

Let's explore two examples.

.. literalinclude:: image_donuts1.py
   :language: python
   :linenos:
   :caption: image_donuts1.py

Donuts shape doesn't have effect of angle.
However, text has effect.

.. figure:: image_donuts1.png
    :width: 500
    :class: with-border
    :align: center

    image_donuts1.png

Technically, ``donuts()`` is a syntax sugar function of ``wedge()``.

fan()
-------

Function fan() draws fan which is part of circle.
In other words, drawing circle from angle-A to angle-B is a fan.

This function takes these arguments.

* xy (tuple[float, float]): X, Y coordinate
* radius (float): radius
* from_angle (float): shape starts
* to_angle (float): shape ends
* angle (float): rotate shape
* style (ShapeStyle)
* text (str): center text
* textstyle (ShapeTextStyle)

As you can see we have 3 angles in arguments.
Please remember, use create shape via ``from_angle`` and ``to_angle``.
After creation, rotate it via ``angle``.

Let's explore two examples.

.. literalinclude:: image_fan1.py
   :language: python
   :linenos:
   :caption: image_fan1.py

First example draws fan from angle(``from_angle``) 0 to angle(``to_angle``) 135.
Second example is same, but it rotate fan via specifying ``angle``. 

.. figure:: image_fan1.png
    :width: 500
    :class: with-border
    :align: center

    image_fan1.png

Technically, ``fan()`` is a syntax sugar function of ``wedge()``.

regularpolygon()
------------------

Function ``regularpolygon()`` draws regular polygon.
You can specify number of vertex from 3 to many.

This function takes these arguments.

* xy (tuple[float, float]): X, Y coordinate
* radius (float): radius of vertices
* num_vertices (int): number of vertices
* angle (float): rotate shape
* style (ShapeStyle)
* text (str): center text
* textstyle (ShapeTextStyle)

Let's explore two examples.

.. literalinclude:: image_regularpolygon1.py
   :language: python
   :linenos:
   :caption: image_regularpolygon1.py

We draw pentagon(5 vertices) and hexagon(6 vertices).

.. figure:: image_regularpolygon1.png
    :width: 500
    :class: with-border
    :align: center

    image_regularpolygon1.png

Providing vertices 2 draws line and huge number such as ``1000,000,000`` draws circle.
But there are no reason to use them.

star()
--------

Function ``regularpolygon()`` draws star.
You need to specify how many external vertices it has.
And also, radius for external vertices and internal vertices.

* xy (tuple[float, float]): X, Y coordinate
* radius_ext (float): external radius
* radius_int (float): internal radius
* num_vertices (int): number of vertices
* angle (float): rotate shape
* style (ShapeStyle)
* text (str): center text
* textstyle (ShapeTextStyle)

Let's explore two examples.

.. literalinclude:: image_star1.py
   :language: python
   :linenos:
   :caption: image_star1.py

Via changing ``num_vertices``, you can draw many type of stars.

.. figure:: image_star1.png
    :width: 500
    :class: with-border
    :align: center

    image_star1.png

wedge()
--------

Function ``wedge()`` draws wedge.
It is a mix of ``donuts()`` and ``fan()``.
You can specify external radius and shape area width.
And also, where drawing start and end.

This function takes these arguments.

* xy (tuple[float, float]): X, Y coordinate
* radius (float): radius
* width (float): width of donuts fill area
* from_angle (float): shape starts
* to_angle (float): shape ends
* angle (float): rotate shape
* style (ShapeStyle)
* text (str): center text
* textstyle (ShapeTextStyle)

Let's explore two examples.

.. literalinclude:: image_wedge1.py
   :language: python
   :linenos:
   :caption: image_wedge1.py

You can specify both ``donts()`` and ``fan()`` arguments for function ``wedge()``.

.. figure:: image_wedge1.png
    :width: 500
    :class: with-border
    :align: center

    image_wedge1.png

You can draw both donuts and fan shape via ``wedge()``.
But functions ``donuts()`` and ``fan()`` are more simple and having easy function name.
We recommend using them for their shapes.

Draw Rectangle Like Shapes
============================

Rectangle like object specifies xy and width/height and other shape specific args.
Both ``arc()`` and ``ellipse()`` are looking similar to circle by shape.
However, there parameters are similar to rectangle.
So, we categorize them to rectangle like shape.

arc()
-------

Function ``arc()`` draws arc.
Arc is looks like line, but it is drawn as shape.
So, you can't specify arrow style.
But you can specify line style via attribute of ``ShapeStyle``.

It takes width and height for underlying transparent ellipse.
And draw visible line over it between specified angles.

This function takes these arguments.

* xy (tuple[float, float]): X, Y coordinate
* radius (float): radius
* width (float): width of donuts fill area
* from_angle (float): arc starts
* to_angle (float): arc ends
* angle (float): rotate arc
* style (ShapeStyle)
* text (str): center text
* textstyle (ShapeTextStyle)

Let's explore two examples.

.. literalinclude:: image_arc1.py
   :language: python
   :linenos:
   :caption: image_arc1.py

How to handle angle is almost same to ``donuts()`` etc.
Please check its explanation for details.
Here is an output.

.. figure:: image_arc1.png
    :width: 500
    :class: with-border
    :align: center

    image_arc1.png


Draw Other Type of Shapes
============================