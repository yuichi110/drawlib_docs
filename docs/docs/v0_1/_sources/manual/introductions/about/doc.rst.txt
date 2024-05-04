===============
About drawlib
===============

Benefit of "Illustration as Code"
==================================

As you know, software and documentations are maintained at many version control systems in these days.
You can easily track diff of code and documentation changes on those environment.
However, achieving same benefit at illustration is difficult.
Because original illustration data is not text but binary.

drawlib provides Illustration as Code to you.
It means

- Same image you get with same code.
- Easy to update, revert, and copy-paste the image.
- Applying same style to line/shape/text accross many illustrations through importing your styles.
- build 100+ codes to 100+ illustrations with ``python -m drawlib <doc root>`` command.

These feature might make you happy on these situations.

- Writing documentation with images
- Writing books with images
- Just for a hobby

As a real example, this documentation contains lots of images which is drawn by this command.
Those image python codes are maintained with text docs on same directory.
When you want to update the image, just update python code and run it again.
It will update the image which the doc shows.

By the way, we introduce API versioning and keeping old APIs on new library versions.
So, you can get same image few years later with latest library.

Because it is Python 
======================

Many people who read this doc might familiar with Python.
You will get benefit of python and its ecosystem on this library of course!!

- create your function for grouping drawing actions
- using loop for repeated drawing
- get help from your IDE (I recommend VSCode and python extensions)
- when having an error on your code, you will get familiar python error messages

So, don't hesitate to try.
Just install and write few codes.
Then you can get your image easily.

Enjoy!!