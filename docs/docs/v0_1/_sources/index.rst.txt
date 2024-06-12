.. drawlib documentation master file, created by
   sphinx-quickstart on Sun Mar 31 22:39:53 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================================
Welcome to the Drawlib Documentation!
=======================================

Drawlib is a pure Python drawing library crafted to facilitate **Illustration as Code** rather than focusing solely on creating polished illustrations. 
Witness Python code in action generating a circular image:

.. figure:: manual/introductions/index/image1.png
    :width: 800
    :class: with-border
    :align: center

    Code makes Illustration

As you can see, we define circle location, size and styles.
Running this code generate the image.

CSS like Styling
====================

At last example, we define style at the derawing item.
It is easy to understand, but repeating styling at items are burden and tending to loose consistency.
We normaly use theme and its styling for changing drawing items style.

Drawlib's style is similar to CSS.
You define style at 1 location and reference it every where.
Then, the style is applied to them automatically.
You don't need to provide detail style for each drawing items.

Here is an example of using style.

.. figure:: manual/introductions/index/image2_default2.png
    :width: 800
    :class: with-border
    :align: center

    CSS like styling feature

This code has around 20+ drawing items which includes background gray area.
You can see variety of drawing styles (default, flat, solid, dashed).
But total code line is less than 100.

Drawlib provides group of styles which is called **theme**.
You can switch theme easily.
For example, applying ``monochrome`` theme make image monochrome.

.. figure:: manual/introductions/index/image2_monochrome.png
    :width: 800
    :class: with-border
    :align: center

You can customize drawlib's pre-defined theme if you wants.
For example, we changed fonts from default "NotoSanserif CJK" to "Raleways".
You don't need to touch content code (same to HTML file concept), but just change theme's styling (same to CSS file concept).
If you wish, you are able to create your own theme.

Good to build lots of images
===============================

In contemporary software development, version control extends beyond code to encompass documentation, all managed seamlessly through Git. 
While I compose technical documents and literature using VSCode and Markdown, hitherto, I relied on PowerPoint for illustration. 
However, this approach lacks compatibility with versioning documentation images.

Enter drawlib, a solution meticulously developed to address this quandary. 
Not only can textual documentation be version-controlled, but illustration code can also be managed through Git, facilitating automation of build tasks via CI/CD pipelines.

.. figure:: manual/introductions/index/image3.png
    :width: 800
    :class: with-border
    :align: center

    Doc image/text build flow.

There are no big difference from markdown document management even if drawlib is added.
If you create your doc from markdown or related one, you can adopt drawlib easily.

By the way, this image itself is created by drawlib.
It might be good real world example of drawlib's illustration.
We build hundreads of these kind of images from image codes with same style for writing books.

Refer to the Quickstart guide for a comprehensive understanding of drawlib's underlying concepts. 
All images within this documentation are generated using drawlib.

.. toctree::
   :maxdepth: 2
   :caption: Introductions:

   manual/introductions/about/doc
   manual/introductions/install/doc
   manual/introductions/lib_design/doc
   manual/introductions/quick_start/doc
   manual/introductions/other_version_docs/doc

.. toctree::
   :maxdepth: 2
   :caption: Foundations:

   manual/foundations/canvas/doc
   manual/foundations/coordinate_align/doc
   manual/foundations/icon/doc
   manual/foundations/image/doc
   manual/foundations/line/doc
   manual/foundations/line_style/doc
   manual/foundations/shape/doc
   manual/foundations/shape_style/doc
   manual/foundations/text/doc
   manual/foundations/theme/doc
   manual/foundations/build_many/doc
   manual/foundations/programming/doc

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics:

   manual/advanced_topics/color/doc
   manual/advanced_topics/font/doc
   manual/advanced_topics/dimage/doc
   manual/advanced_topics/smartarts/doc
   manual/advanced_topics/smartarts_bubblespeech/doc
   manual/advanced_topics/smartarts_sourcecode/doc
   manual/advanced_topics/debug/doc
   manual/advanced_topics/settings/doc
   manual/advanced_topics/cli_options/doc
   manual/advanced_topics/example_flow/doc

.. toctree::
   :maxdepth: 2
   :caption: Themes:

   manual/themes/advanced_topics/doc
   manual/themes/official_default/doc
   manual/themes/official_default2/doc
   manual/themes/official_essentials/doc
   manual/themes/official_monochrome/doc
   manual/themes/customize/doc
   manual/themes/create/doc

.. toctree::
   :maxdepth: 2
   :caption: API Docs:

   api/modules
   api/drawlib
   api/drawlib.v0_1
   api/drawlib.v0_1.private
   api/drawlib.v0_1.private.core

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
