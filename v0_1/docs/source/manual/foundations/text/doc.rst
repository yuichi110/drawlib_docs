===============
Drawing Text
===============

Drawing text requires undersnding of them

* text(): Function for drawing text
* TextStyle: Style class of text
* font: How to specify fonts

We explain them in this page one by one.

text()
=========

drawlib use ``text()`` for drawing text.
It takes these arguments.

* xy (tuple[float, float]): coordinate of drawing point
* text (str): text value
* angle (optional float): angle of text
* style (optional TextStyle): text style

Without style, ``text()`` is very simple.
Here are 2 examples.

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

Right side uses Japanese and specifying angle.

.. figure:: image1.png
    :width: 500
    :class: with-border
    :align: center

    image1.png

Drawlib's default theme uses multi language font ``Noto SanSerif CJK Japanese``.
It is popular SanSerif which supports Chinese Korean Japanese.
As the font name denote it prioritize Japanese, but might not have conflict with Chinese and Korean normally.


TextStyle
===========

TextStyle is style of text.
It posses many attributes, but almost all of them are categorized to "alignment", "text style" and "text background style".

ShapeTextStyle has these attributes.

* halign: Text horizontal alignment. "left", "center", "right"
* valign: Text vertical alignment. "bottom", "center", "top"
* color: text color
* size: text size
* font: text font
* bgalpha: background alpha
* bglwidth: background line width
* bglcolor: background line color
* bglstyle: background line style. "solid", "dashed", "dotted", "dashdot"
* bgfcolor: background fill color

Default alignment is center, center.
And background is not drawn by default.

Here are 2 examples.

.. literalinclude:: image_style1.py
   :language: python
   :linenos:
   :caption: image_style1.py

Left side example configure alignment and text style.
Right side example configure text background style.

.. figure:: image_style1.png
    :width: 500
    :class: with-border
    :align: center

    image_style1.png

In our opinion there are few chance for using text background.
However setting white(or other canvas background color) no-border background is useful for drawing texts over shapes and lines.

Font
======

Drawlib specify font from drawlib's font or your font file.
Drawlib can't use system font which your PC.
Technically drawlib can use system font, but using system font is not good for achieving same result anywhere.
So we don't provide feature for using them.

Drawlib posses these Font classes.

* Font
* FontSanSerif
* FontSerif
* FontMonoSpace
* FontSourceCode
* FontRoboto

They contains popular fonts or fonts we like.
And also, these local language fonts are supported too.

* FontArabic
* FontChinese
* FontJapanese
* FontKorean
* FontThai

If your prefered language is not supported, please request us.
But we can support only OSS free fonts.
Currently we use Google fonts.

If you want to use your font, please provide it via ``FontFile`` class.
We will explain details of font at font doc.
