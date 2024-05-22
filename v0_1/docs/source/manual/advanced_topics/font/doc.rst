=============
Font Classes
=============

Drawlib posses variety of fonts.
Fonts are grouped by Font Classes.
And also you can use your own font through ``FontFile`` class and font files.
Both font and FontFile are mainly used for ``TextStyle`` and ``ShapeTextStyle``.

Here is a list of supported font classes.

- ``Font``: SanSerif and Serif for Alphabet + CJK(Chinese, Japanese, Korean)
- ``FontSansSerif``: SanSerif fonts for Alphabet
- ``FontSerif``: Serif fonts for Alphabet
- ``FontMonoSpace``: Mono space fonts
- ``FontSourcecode``: Subset of FontMonoSpace. It is used for ``dsart.sourcecode()``
- ``FontRoboto``: Roboto fonts for Alphabet

And also, we supports local language fonts.

- ``FontArabic``: Arabic
- ``FontBrahmic``: Fonts which are categorized to Brahmic. India and near countries.
- ``FontChinese``: Chinese
- ``FontJapanese``: Japanese
- ``FontKorean``: Korean
- ``FontThai``: Thai

Each fonts posses these styles.

- ``Light``
- ``Regular``
- ``Bold``

However, few fonts have only 1 or 2 styles.
On that situation, 

If your language font is not supported, please let us know.
We want to support local language fonts as possible as we can.
But the font must be free.

These font size are not small.
So, drawlib download specific font file which you use.
After downloading them, they will be cached on your PC.
The location is inside of drawlib library.


FontFile
============

Before going to explain font classes, we will handle ``FontFile`` class which is used for your own font.
Passing font file to ``FontFile`` class let you use the font for ``text()`` etc.


Font
===========

FontSansSerif
=================

FontSerif
==========

FontRoboto
=============

FontMonoSpace
===============

FontArabic
============