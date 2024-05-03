===============
Canvas
===============

Canvas is drawlib's canvas class.
drawlib draws line/shape/text/image over the canvas.

You don't need to create Canvas instance and calling drawing methods at drawlib.
drawlib holds its default canvas object and you are drawing to it with functions.
drawlib's code should be script rather than object-oriented programming code.

How to use canvas
====================

we have these basic functions for controlling default canvas object.

- ``clear()``: initialize canvas state. Wipe all config and drawing objects
- ``config()``: configure canvas. such as size and background color etc.
- ``title()``: add image title(text)
- ``save()``: export canvas to image file

normally, ``config()`` and ``save()`` will be used all time.
If 1 script file draw only 1 image, you don't need to use ``clear()``.
When you do bulk drawing operation (please check the section), ``clear()`` will be called automatically between script1 and script2.

``save()`` function is very simple.
So, understanding only ``config()`` is enough for normal users.

Grid
===============

You might run illustration code many times for checking how your code will generate image.
After repeating write/check/fix, your illustration creation will finish.
On these try and error, showing grid line might be useful for understanding coordinate and size.
It will help you aligning many objects in one image.

You can enable grid easily with setting ``True`` for option grid.
Default setting is ``False``.

.. literalinclude:: image_grid_1.py
   :language: python
   :linenos:
   :caption: image_grid_1.py

.. figure:: image_grid_1.png
    :width: 300
    :class: with-border
    :align: center

    image_grid_1.png

If you want to apply line style to Grid, just provide LineStyle object.
For example

.. literalinclude:: image_grid_2.py
   :language: python
   :linenos:
   :caption: image_grid_2.py

.. figure:: image_grid_2.png
    :width: 300
    :class: with-border
    :align: center

    image_grid_2.png

Providing ``grid_style`` will make option grid ``True`` since providing style is will of showing grid.
But you can disable it by providing ``grid=False`` of course.


Size
=============

The most important setting of canvas is its size.
Without specifying it, drawlib use its default value.
To control size, you should specify ``width`` and ``height`` at least.
They will be used as maximum shown coordinate of drawing objects.

.. literalinclude:: image_size_1.py
   :language: python
   :linenos:
   :caption: image_size_1.py

.. figure:: image_size_1.png
    :width: 300
    :class: with-border
    :align: center

    image_size_1.png

If you want to draw items in big coordinate, just set big value.

.. literalinclude:: image_size_2.py
   :language: python
   :linenos:
   :caption: image_size_2.py

.. figure:: image_size_2.png
    :width: 300
    :class: with-border
    :align: center

    image_size_2.png

If you want to wide image, make width larger than height.

.. literalinclude:: image_size_3.py
   :language: python
   :linenos:
   :caption: image_size_3.py

.. figure:: image_size_3.png
    :width: 300
    :class: with-border
    :align: center

    image_size_3.png

`config()` will keep previous state if you don't provide its arg.
In this case, canvas will keep its width and height 100 after calling above settings.
arg color accepts text and RGB.
alpha support 0.0(completely transparent) ~ 1.0(no transparency).

DPI and resolution
=====================

DPI (Dot Per Inch) is important concept of drawlib's rendering quality.
But before understanding DPI, you need to understand real implementation of drawlib's canvas size.

In previous examples, you configured ``config(width=100, height=100)`` and ``config(width=200, height=200)``.
You might guess big width/height make big image. It means high resolution.
But it is not truth. Let's check image size.

.. code-block:: none

    $ file image_size_1.png 
    image_size_1.png: PNG image data, 1000 x 1000, 8-bit/color RGBA, non-interlaced

    $ file image_size_2.png
    image_size_2.png: PNG image data, 1000 x 1000, 8-bit/color RGBA, non-interlaced

    $ file image_size_3.png
    image_size_3.png: PNG image data, 1000 x 562, 8-bit/color RGBA, non-interlaced

As you can see, all image's pixel width is 1000.

drawlib uses Matplotlib for its drawing system.
At matplot lib, width/height 1 means 1 inch.

DPI means **how many dots exist in 1 inch**.
So, matplotlib's width 10 and DPI 100 means, 10inch * 100dots. 1000 pixel width.

drawlib's width is used for its coordinate system.
drawlib's width is converted to matplotlib's width 10.
So, ``config(width=100, height=100)`` and ``config(width=200, height=200)`` has no big difference on point of matplotlib's drawing system.

Regarding 3rd example ``config(width=1920, height=1080)``, drawlib change 1920 to 10.
And it try to keep original aspect and calculate matplotlib's height 5.625 (simple math. ``1080 / 1920 * 10``).
And then, the pixel size becomes ``1000 x 562``.

Keeping same matplotlib width is important for consistent size of text and image.
Text size 10 is looks different in 500px and 1000px images.
So, drawlib converts its width to matplotlib's width 10.

To export good resolution image, you can configure DPI.
10 inch x 100 DPI is 1000px. But 10 inch x 200 DPI is 2000px.
Let's check it in below example.

.. literalinclude:: image_dpi_1.py
   :language: python
   :linenos:
   :caption: image_dpi_1.py

.. figure:: image_dpi_1.png
    :width: 300
    :class: with-border
    :align: center

    image_dpi_1.png

.. code-block:: none

    $ file image_dpi_1.png 
    image_dpi_1.png: PNG image data, 2000 x 2000, 8-bit/color RGBA, non-interlaced

After we double DPI, we can get 2 times high resolution data.
But text size is almost same to when we use DPI 100.

Background color and alpha
=============================

drawlib has these default regarding background.

* color: white
* alpha: 1.0 (totaly not transparent)

We can configure them via ``config()`` command.
Let's take a look example.

.. literalinclude:: image_background_1.py
   :language: python
   :linenos:
   :caption: image_background_1.py

.. figure:: image_background_1.png
    :width: 300
    :class: with-border
    :align: center

    image_background_1.png

As you specified, background color becomes orange.
And transparency is 20%.

As you might know, few image format such as jpg can't hold alpha.
drawlib might not warn you, but generate non-transparent image to you.

Save 
========

``save()`` function will save canvas to image file.

If you don't provide args, it will save PNG image which has script file's name.
For example, calling ``save()`` at script ``myimage.py`` will generate ``myimage.png``.
I recommend this because

- You can understand which script make which image easily.
- PNG is OK for normal situation.

But you can provide 

- file name
- extensions (jpg, png, webp)

to this function.
On that time, image will be saved with the name and extensions.
Here is a example.

.. literalinclude:: image_save.py
   :language: python
   :linenos:
   :caption: image_save.py

.. figure:: myimage.webp
    :width: 300
    :class: with-border
    :align: center

    myimage.webp

.. figure:: image_save.jpg
    :width: 300
    :class: with-border
    :align: center

    image_save.jpg

Please be careful.
All file path at drawlib is relative to script file.
Normal python behavior is entry point of the program (where you call python).

This behavior is benefitial for achieving create lots of images on documentation etc.
Where you want to use the illustration, you write the illustration code.
Easy to organize images.

If you prefer traditional python file path, please change relational path to absolute path first.
Then provide it to ``save()`` function.
It works as your wish.
