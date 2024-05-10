===============
Drawing Image
===============

Drawlib uses function ``image()`` for drawing image.
You can specify 

* coordinate
* size
* what you draw
* styling

In this doc, we explain basics of function first.
Then styling and types of original image datas.

image()
==========

We use function ``image()`` for drawing images.
This function takes these arguments.

* xy
* width
* image: File path string, Dimage, PIL.Image.Image
* angle
* style: ImageStyle

Coordinate and alignment is same to other drawing items.
Let's start from example.

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

We draw 3 images which has different xy and width.
Execute the code.

.. figure:: image1.png
    :width: 500
    :class: with-border
    :align: center

    image1.png

As you can see, xy becomes center of image by default.

ImageStyle
==============

Drawing image can be styled with data class ``ImageStyle``.
ImageStyle has these attributes.

* halign: Horizontal Align
* valign: Verteical Align
* lwidth: Line width
* lcolor: Line color
* lstyle: Line style

Let's check image styling with example.
Here is a code which specify stylings.

.. literalinclude:: image2.py
   :language: python
   :linenos:
   :caption: image2.py

The first image changes alignment.
Default alignment is center,center, but left,bottom might be useful sometimes.
Changing image border line at 2nd example.
Default is no border.
The 3rd example changes angle of image.
Executing code generates this output.

.. figure:: image2.png
    :width: 500
    :class: with-border
    :align: center

    image2.png

ImageStyle is not so difficult.

Passing image objects
=========================

Function ``image()`` takes mandatory arg ``image``.
We use file path at previous examples, but also able to use these image objects.

* ``Dimage``
* ``PIL.Image.Image``

Former is our image utility class and latter is famous PIL(Pillow) library.
We mention detail of Dimage at the page, but we show example of how to use it on function image().
Please check PIL by yourself if you want to use.

Here is a example of how to use them.

.. literalinclude:: image3.py
   :language: python
   :linenos:
   :caption: image3.py

Both instances are passed to arg ``image``.
Function ``image()`` will handle them correctly.

We use ``dutil.get_script_relative_path()`` for just getting correct file path.
Drawlib's function always use path **relative path from the script path**.
However normal python code use path from entry point(where you start Python).
This utility function changes the python native path rule to drawlib's path rule.

.. figure:: image3.png
    :width: 500
    :class: with-border
    :align: center

    image3.png

As you can see all 3 arg makes same drawing output.
If you don't modify image, there are no reason to use Dimage and PIL image.
They are useful when you want to apply effect to images.