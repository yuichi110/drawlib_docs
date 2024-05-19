======================
Building many images
======================

Drawlib is designed for creating lots of illust for ducumentation etc.
Here is a typical build process.

.. figure:: ../../introductions/index/image2.png
    :width: 600
    :class: with-border
    :align: center

    Build many images

As you can see you can achieve

- declare styling at 1 or few code files
- each image codes file imports them and use the style
- run all image codes under specified directory and generate images

Directory level build
========================

Suppose you have image code files on directory ``images``.
You can build each image with ``python <code file>`` command.
But you can only specify one image code in this style.

If you want to achieve build all images in specified directory, you can use this command.

.. code-block:: none

   $ python -m drawlib <directory_name>

Then, drawlib builds executes all python codes which has extension ``.py`` in the directory and its sub directories.

Order of execution
====================

The directory contains many code files.
Drawlib executes them in this order

1. Starting from shallow directory
2. String sort order of python

We recommend each code file doesn't depends on other codes which are not specified.
``b.py`` will be executed after ``a.py``.
But ``b.py`` shouldn't depends on ``a.py``.
Because ``b.py`` can be executed as ``python directory/b.py`` on that time, ``a.py`` will not be executed.

Execute other drawlib codes first via dexec()
================================================

There are many chances that some code files need to be executed before executing the code file.
For example, run styling code file before executing drawing codes.
On that situation, function ``dexec()`` is useful.
The function name come from "drawlib execute".

This function runs specified code or directory first before moving to next line on the original code file.
This behavior is similar to ``import``.
But there are no feature that imports functions and classes.
Just run the specified files.

Drawlib posses cache feature on these items.

- theme and its styles
- Dimage (image data)

At common code, cache them.
After that drawing code call the common codes.
This procedure assure the drawing code can use cached styles and images.

Function ``dexec()`` can call same code file again.
However, they are executed only at first time.
Second time, execution will be skipped.
There are no chance to make cache twice.
We recommend calling ``dexec()`` at all drawing codes which uses the cache.
Cache will be created on any code files which calls ``dexec()``.

Let's check the behavior with simple example.

Real World Example
=====================

For example, you have these structure

.. code-block:: none

   mydoc ---+--- .drawlib ---+--- mystyle.py
            |                +--- myimage.py
            |                +--- lots of icon images
            |
            +--- index.rst or index.md
            +--- image1.py
            +--- image2.py
            |
            +--- chap1 ------+--- chap1.rst or chap1.md
                             +--- image1.py
                             +--- image2.py

You define common style at `mystyle.py` and load icon images at `myimage.py`.
I like using directory `.drawlib` as holding common codes and images, but it is not a rule.
You can use any directory name.

After defining them, you can use them at all other image code files.
BTW, same file name can be used if directory is different as you can see above.

OK, let's walk through how to acieve bulk image creation.

set cache at common code
============================

run the common code and get cache
===================================

bulk build
=============