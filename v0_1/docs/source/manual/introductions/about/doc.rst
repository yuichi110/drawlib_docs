===============
About drawlib
===============

Drawlib is a pure Python drawing library designed to facilitate **Illustration as Code**, rather than focusing solely on creating polished illustrations. 
For instance, consider the following Python code:

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

Execute it with the python command:

.. code-block:: none

   $ python image1.py

This will generate an image file.

.. figure:: image1.png
    :width: 450
    :class: with-border
    :align: center

    image1.png

As illustrated, drawlib generates an image corresponding to your code.
Normally, you don't need to specify detailed styles. The theme's style will be automatically applied when it's not provided.


Benefit of "Illustration as Code"
==================================

In today's world, many technical documents are managed using version control systems such as Git. 
However, managing illustrations poses a challenge as they are typically binary files rather than text-based. 
Drawlib offers a solution by generating illustrations from pure Python code. 
This means that if you create your illustrations using Python and drawlib, you can manage them using version control systems too.

Drawlib is optimized for drawing a large number of illustrations with a consistent style. 
This can be easily achieved by creating a theme file (which is simply Python code) and importing it into your illustration codes (also Python code). 
Here is a typical use case of drawlib.

.. figure:: ../index/image3.png
    :width: 600
    :class: with-border
    :align: center

    image2.png

As a real-world example, almost all of the documentation images are created by drawlib. 
The build flow is almost the same as the image above. 
We build images using drawlib first, then build the document via Sphinx, and finally publish it to the Internet. 
These images are built by scripts locally for quickly checking draw results. 
We run CI/CD when code is committed to the GitHub repository to reduce human operation costs and avoid human errors.

Drawlib adopts the ``theme`` feature, which is similar to a slide theme. 
When you change the theme, the default theme style is automatically applied to all images. 
If you want to change the style slightly, modifying the theme will affect all of your images that reference the theme. 
This is beneficial for maintaining consistency of image style and achieving good styling with less effort.


Because it is Python 
======================

Many people who read this document might be familiar with Python. 
You will benefit from Python and its ecosystem with this library, such as:

- creating your functions for grouping drawing actions
- using loops for repeated drawing
- getting help from your IDE (I recommend VSCode and Python extensions)
- when encountering an error in your code, you will receive familiar Python error messages

You don't need to learn another programming language or DSL(Domain Specific Language) to achieve illustration as code. 

If you are familiar with Python, you might be able to understand how to use drawlib with just a few hours of struggling. 
The design of drawlib is consistent and Pythonic.