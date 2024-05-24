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
On that situation, drawlib lacks few styles too.

By the way, these font file size are not small.
So, drawlib doesn't include them when you did ``pip install``.
But drawlib downloads specific font file when you use it first time.
After downloading them, they will be cached on your PC.
You can delete cache via utility module ``dutil``.


FontFile
============

Before going to explain font classes, we will handle ``FontFile`` class which is used for your own font.
Passing font file to ``FontFile`` class let you use the font for ``text()`` etc.

.. literalinclude:: image_file.py
   :language: python
   :linenos:
   :caption: image_file.py


.. figure:: image_file.png
    :width: 600
    :class: with-border
    :align: center

    Using font file

Font
===========

Class ``Font`` contains these fonts.

- ``SANSSERIF_LIGHT``: Noto SansSerif CJK(Chinese, Japanese, Korean)
- ``SANSSERIF_REGULAR``
- ``SANSSERIF_BOLD``
- ``SERIF_LIGHT``: Noto Serif CJK Japanese
- ``SERIF_REGULAR``
- ``SERIF_BOLD``

Default theme's default font is ``Font.SANSSERIF_REGULAR``.
We choose them since font shape is standard and population coverage is large.

.. figure:: image_Font.png
    :width: 600
    :class: with-border
    :align: center

    class Font

FontSansSerif
=================

Class ``FontSansSerif`` contains these fonts.

- ``LATO_LIGHT``
- ``LATO_REGULAR``
- ``LATO_BOLD``
- ``RALEWAYS_LIGHT``
- ``RALEWAYS_REGULAR``
- ``RALEWAYS_BOLD``
- ``MONTSERRAT_LIGHT``
- ``MONTSERRAT_REGULAR``
- ``MONTSERRAT_BOLD``
- ``OSWALD_LIGHT``
- ``OSWALD_REGULAR``
- ``OSWALD_BOLD``
- ``POPPINS_LIGHT``
- ``POPPINS_REGULAR``
- ``POPPINS_BOLD``

It covers popular SansSerif fonts for alphabet languages.

.. figure:: image_FontSansSerif.png
    :width: 600
    :class: with-border
    :align: center

    class FontSansSerif

FontSerif
==========

Class ``FontSerif`` contains these fonts.

- ``COURIER_REGULAR``
- ``COURIER_BOLD``
- ``MERRIWEATHER_LIGHT``
- ``MERRIWEATHER_REGULAR``
- ``MERRIWEATHER_BOLD``
- ``PLATYPI_LIGHT``
- ``PLATYPI_REGULAR``
- ``PLATYPI_BOLD``
- ``PLAYFAIRDISPLAY_LIGHT``
- ``PLAYFAIRDISPLAY_REGULAR``
- ``PLAYFAIRDISPLAY_BOLD``

It covers popular Serif fonts for alphabet languages.

.. figure:: image_FontSerif.png
    :width: 600
    :class: with-border
    :align: center

    class FontSansSerif

FontRoboto
=============

Class ``FontRoboto`` contains these fonts.

- ``ROBOTO_LIGHT``
- ``ROBOTO_REGULAR``
- ``ROBOTO_BOLD``
- ``SERIF_LIGHT``
- ``SERIF_REGULAR``
- ``SERIF_BOLD``
- ``MONO_LIGHT``
- ``MONO_REGULAR``
- ``MONO_BOLD``
- ``CONDENSED_LIGHT``
- ``CONDENSED_REGULAR``
- ``CONDENSED_BOLD``
- ``SLAB_LIGHT``
- ``SLAB_REGULAR``
- ``SLAB_BOLD``

Roboto is famous and popular free font.
It provides many styles.

.. figure:: image_FontRoboto.png
    :width: 600
    :class: with-border
    :align: center

    class FontSansSerif

FontMonoSpace
===============

Class ``FontMonoSpace`` contains these fonts.

- ``COURIER_REGULAR``
- ``COURIER_BOLD``
- ``ROBOTO_MONO_LIGHT``
- ``ROBOTO_MONO_REGULAR``
- ``ROBOTO_MONO_BOLD``
- ``SOURCECODEPRO_LIGHT``
- ``SOURCECODEPRO_REGULAR``
- ``SOURCECODEPRO_BOLD``
- ``SOURCEHANCODEJP_LIGHT``
- ``SOURCEHANCODEJP_REGULAR``
- ``SOURCEHANCODEJP_BOLD``

It covers popular mono space fonts.
Almost all are for alphabet, but Source Han Code JP supports Japanese.

.. figure:: image_FontMonoSpace.png
    :width: 600
    :class: with-border
    :align: center

    class FontSansSerif

FontArabic
============

Class ``FontArabic`` contains these fonts.

- ``SANSSERIF_LIGHT``
- ``SANSSERIF_REGULAR``
- ``SANSSERIF_BOLD``
- ``KUFI_LIGHT``
- ``KUFI_REGULAR``
- ``KUFI_BOLD``
- ``NASKH_LIGHT``
- ``NASKH_REGULAR``
- ``NASKH_BOLD``

It covers Arabic fonts.

.. figure:: image_FontArabic.png
    :width: 600
    :class: with-border
    :align: center

    class FontArabic

FontBrahmic
============

Class ``FontBrahmic`` contains these fonts.

- ``BENGALI_SANSSERIF_LIGHT``
- ``BENGALI_SANSSERIF_REGULAR``
- ``BENGALI_SANSSERIF_BOLD``
- ``BENGALI_SERIF_LIGHT``
- ``BENGALI_SERIF_REGULAR``
- ``BENGALI_SERIF_BOLD``
- ``DEVANAGARI_SANSSERIF_LIGHT``
- ``DEVANAGARI_SANSSERIF_REGULAR``
- ``DEVANAGARI_SANSSERIF_BOLD``
- ``DEVANAGARI_SERIF_LIGHT``
- ``DEVANAGARI_SERIF_REGULAR``
- ``DEVANAGARI_SERIF_BOLD``
- ``TAMIL_SANSSERIF_LIGHT``
- ``TAMIL_SANSSERIF_REGULAR``
- ``TAMIL_SANSSERIF_BOLD``
- ``TAMIL_SERIF_LIGHT``
- ``TAMIL_SERIF_REGULAR``
- ``TAMIL_SERIF_BOLD``
- ``TELUGU_SANSSERIF_LIGHT``
- ``TELUGU_SANSSERIF_REGULAR``
- ``TELUGU_SANSSERIF_BOLD``
- ``TELUGU_SERIF_LIGHT``
- ``TELUGU_SERIF_REGULAR``
- ``TELUGU_SERIF_BOLD``

It covers characters which delived from Brahmic.

.. figure:: image_FontBrahmic.png
    :width: 600
    :class: with-border
    :align: center

    class FontBrahmic

FontChinese
============

Class ``FontChinese`` contains these fonts.

- ``SIMPLIFIED_SANSSERIF_LIGHT``
- ``SIMPLIFIED_SANSSERIF_REGULAR``
- ``SIMPLIFIED_SANSSERIF_BOLD``
- ``SIMPLIFIED_SERIF_LIGHT``
- ``SIMPLIFIED_SERIF_REGULAR``
- ``SIMPLIFIED_SERIF_BOLD``
- ``TRADITIONAL_SANSSERIF_LIGHT``
- ``TRADITIONAL_SANSSERIF_REGULAR``
- ``TRADITIONAL_SANSSERIF_BOLD``
- ``TRADITIONAL_SERIF_LIGHT``
- ``TRADITIONAL_SERIF_REGULAR``
- ``TRADITIONAL_SERIF_BOLD``
- ``HONGKONG_SANSSERIF_LIGHT``
- ``HONGKONG_SANSSERIF_REGULAR``
- ``HONGKONG_SANSSERIF_BOLD``
- ``HONGKONG_SERIF_LIGHT``
- ``HONGKONG_SERIF_REGULAR``
- ``HONGKONG_SERIF_BOLD``

Chinese has many character types.

.. figure:: image_FontChinese.png
    :width: 600
    :class: with-border
    :align: center

    class FontChinese

FontJapanese
============

Class ``FontJapanese`` contains these fonts.

- ``SANSSERIF_LIGHT``
- ``SANSSERIF_REGULAR``
- ``SANSSERIF_BOLD``
- ``SERIF_LIGHT``
- ``SERIF_REGULAR``
- ``SERIF_BOLD``
- ``MPLUS1P_LIGHT``
- ``MPLUS1P_REGULAR``
- ``MPLUS1P_BOLD``
- ``MPLUSROUNDED1C_LIGHT``
- ``MPLUSROUNDED1C_REGULAR``
- ``MPLUSROUNDED1C_BOLD``
- ``SAWARABI_GOTHIC``
- ``SAWARABI_MINCHO``

It covers popular japanese free fonts.

.. figure:: image_FontJapanese.png
    :width: 600
    :class: with-border
    :align: center

    class FontJapanese

FontKorean
============

Class ``FontKorean`` contains these fonts.

- ``SANSSERIF_LIGHT``
- ``SANSSERIF_REGULAR``
- ``SANSSERIF_BOLD``
- ``SERIF_LIGHT``
- ``SERIF_REGULAR``
- ``SERIF_BOLD``

It covers popular Serif fonts for alphabet languages.

.. figure:: image_FontKorean.png
    :width: 600
    :class: with-border
    :align: center

    class FontKorean

FontThai
============

Class ``FontThai`` contains these fonts.

- ``SANSSERIF_LIGHT``
- ``SANSSERIF_REGULAR``
- ``SANSSERIF_BOLD``
- ``SERIF_LIGHT``
- ``SERIF_REGULAR``
- ``SERIF_BOLD``

It covers Thai fonts.

.. figure:: image_FontThai.png
    :width: 600
    :class: with-border
    :align: center

    class FontThai

Request for Adding Fonts
=========================

Please let us know which font you want to have in our library.
If request meets the criteria, we will add it to next new release.

- The font must be free
- The font works on drawlib (Emoji font doesn't work well now.)
- Your language is not supported. We want to add font even if the language is minor.
- The font is popular globally
- The local language font is popular on the region

We recommend to use ``FontFile()`` first before requesting adding fonts officially.
Currently, we are not have fancy fonts.
