======================
Drawlib Overview
======================

Drawing illustrations can be a complex task. 
To simplify this process, drawlib offers a variety of APIs for drawing icons, images, lines, shapes, and text, along with their respective styles. 
However, you don't need to memorize every detail to start drawing. 
By grasping the design of the drawlib library, you can write code efficiently by referring to classes, functions, and their options through IDE assistance. 
If you encounter difficulties, our API documentation provides comprehensive guidance on usage.

Abstract API Structure
======================

Drawlib consists of the following APIs:

- Fundamental classes and functions, such as canvas manipulation methods like ``save()`` and ``config()``.
- Drawing functions, including ``circle()`` and ``line()``.
- Style classes, like ``ShapeStyle`` and ``LineStyle``.
- Advanced classes and functions that internally utilize the aforementioned APIs.

.. figure:: image1.png
    :width: 600
    :class: with-border
    :align: center

    image1.png

The most intricate portion of the image above, divided into five categories, represents the core of drawlib with numerous APIs. 
Despite this complexity, the function arguments and style classes remain largely consistent.

Once you grasp the fundamental concepts of the library, predicting the results of functions and arguments becomes intuitive.
