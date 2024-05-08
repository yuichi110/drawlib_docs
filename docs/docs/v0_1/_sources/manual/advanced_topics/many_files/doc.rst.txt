======================
Building many images
======================

drawlib is designed for creating lots of illust for ducumentation etc.
On those kind of situation, these feature is very useful.

- declare styling at 1 or few code files
- each image code file imports them and use the style
- run all image codes under specified directory and generate images

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