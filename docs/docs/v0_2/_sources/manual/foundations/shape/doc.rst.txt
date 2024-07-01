===============
Drawing Shape
===============

Drawlib provides a variety of functions for drawing shapes, from basic circles and rectangles to more specialized shapes like bubblespeech and chevrons. 
These functions are categorized into three types based on the shapes they draw:

* Circle-like shape: Specify ``xy`` and ``radius``
* Rectangle-like shape: Specify ``xy`` and ``width``, ``height``
* Other shapes: Arrow(from ``xy1`` to ``xy2``), Polygon(connects ``xys`` and filling) etc.

Circle-like Shapes
--------------------

Functions that draw circle-like shapes include:

* ``circle()``
* ``donuts()``
* ``fan()``
* ``regularpolygon()``
* ``star()``
* ``wedge()``

Rectangle-like Shapes
-----------------------

Functions that draw rectangle-like shapes include:

* ``arc()``
* ``chevron()``
* ``ellipse()``
* ``parallelogram()``
* ``rectangle()``
* ``rhombus()``
* ``trapezoid()``
* ``triangle``

Other Shapes
--------------

Functions that draw other types of shapes include:

* ``arrow()``
* ``polygon()``
* ``shape()``

Let's explore all of these functions, except ``shape()`` which is covered on another page. 
The ``shape()`` function is useful for drawing custom shapes.

By default, all shapes are horizontally and vertically centered. 
This can be changed using the ``ShapeStyle()`` object. 
However, ``arrow()`` and ``polygon()`` do not have alignment attributes and will ignore these settings.

We'll discuss styling with ``ShapeStyle`` and ``ShapeTextStyle`` on another page.


Text of Shapes
=================

All shapes can have text at their center. 
Before diving into each shape, let's explain this common feature.

Shape functions can take these three optional arguments:

* ``text``: The text to display at the center of the shape.
* ``textsize``: The font size of the text.
* ``textstyle``: The style of the center text. You can configure the size and other properties here as well.

All of these arguments are optional. 
If you do not provide any value for text, no text will be shown.
We recommend setting font size at textstyle rather than textsize.


Draw Circle-like Shapes
=========================

Circle-like shapes specify ``xy``, ``radius``, and other shape-specific arguments.

circle()
---------

The ``circle()`` function draws a circle and takes the following arguments:

* xy : X, Y coordinates.
* radius: Radius of the circle.
* angle: Angle which affects the text inside the circle.
* style: Style of the circle.
* text: Text displayed at the center of the circle.
* textsize: The font size of the text.
* textstyle: The style of the center text

Let's explore two examples.

.. literalinclude:: image_circle1.py
   :language: python
   :linenos:
   :caption: image_circle1.py

The circle shape itself does not have an angle effect, but the text inside does.

Executing the above script generates the following output:

.. figure:: image_circle1.png
    :width: 600
    :class: with-border
    :align: center

    circle()

donuts()
---------

The ``donuts()`` function draws a donut-like shape. 
This shape is defined by an external radius and the width of the filled area, meaning the internal radius is calculated as ``external radius - width``.

This function takes these arguments.

* xy : X, Y coordinates.
* radius: Radius of the donuts.
* width: Width of donuts fill area
* angle: Angle which affects the text inside the donuts.
* style: Style of the donuts.
* text: Text displayed at the center of the donuts.
* textsize: The font size of the text.
* textstyle: The style of the center text

Let's explore two examples.

.. literalinclude:: image_donuts1.py
   :language: python
   :linenos:
   :caption: image_donuts1.py

By adjusting the ``radius`` and ``width`` arguments, you can control the size and thickness of the donut shape.
Executing the above script generates donut shapes with centered text, showing the usage of various arguments.

.. figure:: image_donuts1.png
   :width: 600
   :class: with-border
   :align: center

   donuts()

The ``donuts()`` function is essentially a simplified wrapper around the ``wedge()`` function, providing an easy way to draw donut shapes without needing to handle the internal radius calculations manually.


fan()
-------

The ``fan()`` function draws a fan shape, which is a sector of a circle. In other words, it creates a part of a circle from one angle to another.

* xy : X, Y coordinates.
* radius: Radius of the fan.
* from_angle: The starting angle of the fan.
* to_angle: The ending angle of the fan.
* angle: Angle of the fan.
* style: Style of the fan.
* text: Text displayed at the center of the fan.
* textsize: The font size of the text.
* textstyle: The style of the center text

There are three angle-related arguments:

* ``from_angle``: Defines where the fan shape starts.
* ``to_angle``: Defines where the fan shape ends.
* ``angle``: Rotates the entire fan shape after it is created.

Let's explore two examples.

.. literalinclude:: image_fan1.py
   :language: python
   :linenos:
   :caption: image_fan1.py

By adjusting the from_angle, to_angle, and angle arguments, you can create and position the fan shape as desired.

First example draws fan from angle(``from_angle``) 0 to angle(``to_angle``) 135.
Second example is same, but it rotate fan via specifying ``angle``. 

Executing the above script generates fan shapes with centered text, showing the usage of various arguments.

.. figure:: image_fan1.png
    :width: 600
    :class: with-border
    :align: center

    fan()

The ``fan()`` function is essentially a simplified wrapper around the ``wedge()`` function, making it easy to draw fan shapes by specifying start and end angles, and then optionally rotating the shape.

regularpolygon()
------------------

The ``regularpolygon()`` function draws a regular polygon with a specified number of vertices.

This function takes these arguments.

* xy : X, Y coordinates.
* radius: Radius of the regularpolygon.
* num_vertices: Number of vertices of the polygon (must be 3 or more).
* angle: Angle of the regularpolygon.
* style: Style of the regularpolygon.
* text: Text displayed at the center of the regularpolygon.
* textsize: The font size of the text.
* textstyle: The style of the center text

Here are two examples demonstrating the use of ``regularpolygon()``:

.. literalinclude:: image_regularpolygon1.py
   :language: python
   :linenos:
   :caption: image_regularpolygon1.py

Executing the above script generates regular polygons with centered text, demonstrating the usage of various arguments.

.. figure:: image_regularpolygon1.png
    :width: 600
    :class: with-border
    :align: center

    regularpolygon()

The ``regularpolygon()`` function allows you to specify the number of vertices from 3 upwards to create polygons of various shapes.


star()
--------

The ``star()`` function draws a star shape with a specified number of external vertices.

This function takes these arguments.

* xy : X, Y coordinates.
* radius_ext: Radius of the circle circumscribing the outermost vertices of the star.
* radius_int: Radius of the circle circumscribing the innermost vertices of the star.
* num_vertices: Number of external vertices of the star (must be 3 or more).
* angle: Angle of the star.
* style: Style of the star.
* text: Text displayed at the center of the star.
* textsize: The font size of the text.
* textstyle: The style of the center text

Here are two examples demonstrating the use of ``star()``:

.. literalinclude:: image_star1.py
   :language: python
   :linenos:
   :caption: image_star1.py

The ``star()`` function allows you to specify the number of external vertices to create stars of different shapes and sizes.
Executing the above script generates stars with centered text, demonstrating the usage of various arguments.

.. figure:: image_star1.png
    :width: 600
    :class: with-border
    :align: center

    star()

wedge()
--------

The ``wedge()`` function draws a wedge shape, which is a combination of a donut (ring) and a fan (sector of a circle).

This function takes these arguments.

* xy : X, Y coordinates.
* radius: Radius of the wedge.
* width : width of donuts fill area
* from_angle: Starting angle of the wedge.
* to_angle: Ending angle of the wedge.
* angle: Angle of the wedge.
* style: Style of the wedge.
* text: Text displayed at the center of the wedge.
* textsize: The font size of the text.
* textstyle: The style of the center text

Here is an example demonstrating the use of ``wedge()``:

.. literalinclude:: image_wedge1.py
   :language: python
   :linenos:
   :caption: image_wedge1.py

Executing the above script generates a wedge shape with centered text, demonstrating the usage of various arguments.

.. figure:: image_wedge1.png
    :width: 600
    :class: with-border
    :align: center

    wedge()

The ``wedge()`` function allows you to specify the radius, width, starting angle, and ending angle to create wedge shapes, which are useful for visualizing segments of circles with customizable styles and text.


Draw Rectangle Like Shapes
============================

Rectangle-like shapes in Drawlib are defined using X, Y coordinates along with width and height parameters. 
These shapes, such as ``arc()`` and ``ellipse()``, resemble rectangles in their parameterization despite their curved appearances, hence they are categorized as rectangle-like shapes.

arc()
-------

The ``arc()`` function is used to draw arcs.

An arc resembles a line but is drawn as a shape, thus arrow styles cannot be specified. 
However, you can define the line style using attributes of ``ShapeStyle``.

This function requires the following arguments:

- xy: X, Y coordinates
- width: Width of the underlying ellipse
- height: Height of the underlying ellipse
- from_angle: Starting angle of the arc
- to_angle: Ending angle of the arc
- angle: Rotation angle of the arc
- style: Style of the arc
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples.

.. literalinclude:: image_arc1.py
   :language: python
   :linenos:
   :caption: image_arc1.py

Handling angles is similar to functions like ``donuts()``. 
Please refer to its explanation for more details. 
Here's an example output:

.. figure:: image_arc1.png
    :width: 600
    :class: with-border
    :align: center

    arc()

chevron()
-------------

The ``chevron()`` function draws a chevron shape. 
In addition to specifying width and height, it allows you to define the angle of the bottom-left corner using corner_angle. 
The shape of the chevron varies based on this parameter.

This function takes the following arguments:

- xy: X, Y coordinates
- width: Width of the chevron
- height: Height of the chevron
- corner_angle: Angle of the bottom-left corner
- mirror: Optionally reverses the chevron horizontally (default is False)
- angle: Rotation angle of the chevron
- style: Style of the chevron
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples:

.. literalinclude:: image_chevron1.py
   :language: python
   :linenos:
   :caption: image_chevron1.py

The shape of the chevron is influenced by ``corner_angle``. 
When ``mirror`` is set to True, the chevron is horizontally reversed. 
Here is an example output:

.. figure:: image_chevron1.png
    :width: 600
    :class: with-border
    :align: center

    chevron()

ellipse()
-----------

The ``ellipse()`` function draws an ellipse. 
If the width and height are identical, it behaves similarly to the ``circle()`` function.

This function accepts the following arguments:

- xy: X, Y coordinates
- width: Width of the ellipse
- height: Height of the ellipse
- angle: Rotation angle of the ellipse
- style: Style of the ellipse
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples:

.. literalinclude:: image_ellipse1.py
   :language: python
   :linenos:
   :caption: image_ellipse1.py

Here is an example output:

.. figure:: image_ellipse1.png
    :width: 600
    :class: with-border
    :align: center

    ellipse()

parallelogram()
------------------

The ``parallelogram()`` function draws a parallelogram shape. 
It allows you to specify the angle of the bottom-left corner using ``corner_angle``. 
Additionally, you can mirror the shape horizontally by setting the ``mirror`` parameter to True.

This function accepts the following arguments:

- xy: X, Y coordinates
- width: Width of the parallelogram
- height: Height of the parallelogram
- corner_angle: Angle of the bottom-left corner
- mirror: Optionally reverses the parallelogram horizontally (default is False)
- angle: Rotation angle of the parallelogram
- style: Style of the parallelogram
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples.

.. literalinclude:: image_parallelogram1.py
   :language: python
   :linenos:
   :caption: image_parallelogram1.py

Here is an example output:

.. figure:: image_parallelogram1.png
    :width: 600
    :class: with-border
    :align: center

    parallelogram()


rectangle()
-------------

The ``rectangle()`` function draws a rectangle shape. 
It allows you to specify the radius of the rounded corners using the ``r`` parameter.

This function accepts the following arguments:

- xy: X, Y coordinates
- width: Width of the rectangle
- height: Height of the rectangle
- r: Radius of the rounded corners (default is 0, resulting in sharp corners)
- angle: Rotation angle of the rectangle
- style: Style of the rectangle
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples:

.. literalinclude:: image_rectangle1.py
   :language: python
   :linenos:
   :caption: image_rectangle1.py

Here is an example output:

.. figure:: image_rectangle1.png
    :width: 600
    :class: with-border
    :align: center

    rectangle()

rhombus()
-----------

The ``rhombus()`` function draws a rhombus shape, which is a diamond-like figure with equal sides.

This function accepts the following arguments:

- xy: X, Y coordinates
- width: Width of the rhombus
- height: Height of the rhombus
- angle: Rotation angle of the rhombus
- style: Style of the rhombus
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples:

.. literalinclude:: image_rhombus1.py
   :language: python
   :linenos:
   :caption: image_rhombus1.py

Here is an example output:

.. figure:: image_rhombus1.png
    :width: 600
    :class: with-border
    :align: center

    rhombus()

trapezoid()
-------------

The ``trapezoid()`` function draws a trapezoid shape, which has two different widths at its top and bottom edges. 
The positioning of the top side relative to the bottom side can be adjusted using the ``top_width``, ``bottom_width``, and optionally ``top_start`` parameters.

This function takes these arguments.

- xy: X, Y coordinates
- width: Width of the trapezoid
- height: Height of the trapezoid
- bottom_width: Width of the bottom side of the trapezoid
- top_width: Width of the top side of the trapezoid
- top_start: Optional parameter to specify where the top side starts (default places the top side centered). If set to 0, the top side starts at the same position as the bottom side.
- angle: Rotation angle of the trapezoid
- style: Style of the trapezoid
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples:

.. literalinclude:: image_trapezoid1.py
   :language: python
   :linenos:
   :caption: image_trapezoid1.py

Here is an example output:

.. figure:: image_trapezoid1.png
    :width: 600
    :class: with-border
    :align: center

    trapezoid()

triangle()
------------

The ``triangle()`` function draws a triangle shape. 
It has an optional parameter ``topvertex_xpos`` to specify where the top vertex is positioned horizontally.
If not specified, the triangle is drawn as an isosceles triangle with the top vertex aligned at the center of its width.

This function accepts the following arguments:

- xy: X, Y coordinates
- width: Width of the triangle
- height: Height of the triangle
- topvertex_xpos: Optional parameter to specify the horizontal position where the top vertex is pointed
- angle: Rotation angle of the triangle
- style: Style of the triangle
- text: Centered text
- textsize: Font size of the text
- textstyle: Style of the centered text

Let's explore two examples:

.. literalinclude:: image_triangle1.py
   :language: python
   :linenos:
   :caption: image_triangle1.py

Here is an example output:

.. figure:: image_triangle1.png
    :width: 600
    :class: with-border
    :align: center

    triangle()

In this example, inner text is drawn at the center of the right triangle shape. 
However, the text extends beyond the shape's boundaries. 
In such situations, you can adjust the position where the text is drawn by specifying the ``xy_shift`` attribute of ``ShapeTextStyle``. 
For further details, refer to the shape style documentation.

Draw Other Type of Shapes
============================

arrow()
---------

The ``arrow()`` function draws an arrow shape between two points defined by ``xy1`` (start point) and ``xy2`` (end point). 
You can customize the arrow's tail and head sizes and styles.

This function accepts the following arguments:

- xy1: Start point coordinates (x1, y1)
- xy2: End point coordinates (x2, y2)
- tail_width: Width of the arrow's tail (not the head)
- head_width: Width of the arrow's head
- head_length: Length of the arrow's head
- head_style (optional): Style of the arrow's head (``"->"``, ``"<-"``, ``"<->"`` for different configurations)
- style (optional): Style of the arrow
- text (optional): Centered text
- textstyle (optional): Style of the centered text

Let's explore an example:

.. literalinclude:: image_arrow1.py
   :language: python
   :linenos:
   :caption: image_arrow1.py

Here is an example output:

.. figure:: image_arrow1.png
    :width: 600
    :class: with-border
    :align: center

    arrow()

In the ``arrow()`` function, the angle of the arrow is determined automatically by its start and end points. 
The function does not use the alignment attributes (``halign`` and ``valign``) from ``ShapeStyle``.

polygon()
-----------

The ``polygon()`` function draws a shape that connects specified points to form a polygon. 
The start point and end point are automatically connected.

This function accepts the following arguments:

- xys: List of tuples specifying the points of the polygon [(x1, y1), (x2, y2), ..., (xn, yn)]
- style (optional): Style of the polygon
- text (optional): Centered text
- textstyle (optional): Style of the centered text

Let's explore an example:

.. literalinclude:: image_polygon1.py
   :language: python
   :linenos:
   :caption: image_polygon1.py

Here is an example output:

.. figure:: image_polygon1.png
    :width: 600
    :class: with-border
    :align: center

    polygon()

The ``polygon()`` function does not use an angle argument because the shape's orientation is determined by the order of the specified points. 
If you prefer to draw shapes with a standard coordinate system and angle features, consider using the ``shape()`` function.