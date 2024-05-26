=================
Dimage
=================

Dimage is a image data class of drawlib.
It provides 2 features.

- Effecting images
- Cache (load data one place, use it many places)

Cache
=========

Dimage posses class attribute ``cache``.
The cache posses instance of ``DimageCache`` and it provides these methods.

- ``has(name:str)``: Whether posses cache or not 
- ``set(name:str, image:str|Dimage|PIL.Image)``: Cache image data with specified name
- ``list()``: get all cache names
- ``get(name:str)``: get cache data from name
- ``delete(name:str)``: delete cache

You will not create ``DimageCache`` instance by yourself.
Just understanding accessing cache through ``Dimage.cache`` and the provided methods are same to style cache feature of ``dtheme``.
Here is an example.

.. literalinclude:: image_cache.py
   :language: python
   :linenos:
   :caption: image_cache.py

In this example, we make cache first with ``set()``.
It takes image arg and all of its types are converted to Dimage internally.

And then, get the cache data by specifying name.
Return data is copied one.
So, changing data doesn't effects cache content.
But in the first place, you can't change dimage data like str.
Here is an output.

.. figure:: image_cache.png
    :width: 600
    :class: with-border
    :align: center

The most popular usage is loading to cache at common file and use it at every where.
If you specify file name at each illustration code file, changing image path and name are burden.
However, if you use cache, only changing location is common code.

Things Controlled by image()
==============================

Dimage is helper for function ``image()``.
So, Dimage doesn't have features which ``image()`` has.
These features are not implemented.

- rotate: Option ``angle``
- add border: Attribute ``lwidth`` and ``lcolor`` of ``ImageStyle``.

Save
======

Dimage can save its data to file without using drawlib's canvas.
``save()`` method does this.
It takes mandatory arg ``file``.
Arg ``file`` of Canvas's ``save()`` is optional, but Dimage's ``save()`` requires it.

If you provide relative path, image file is save to relative to script path.
Absolute path will work also.

Get Image Pixel Size 
=======================

You can get original image size through method ``get_image_size()``.
It returns tuple of width and height.
This function might be used with ``resize()`` and ``trim()``.

Resizing and Changing Aspect
===============================

Method ``resize()`` takes 2 arguments ``width`` and ``height``.
They are not size on drawlib's canvas but original data pixel size.

Before resizing, you can check original width and height with method ``resize()``.
If you keep ratio between width and height, the original image size becomes big and small with keeping original aspect.
If you want to change aspect, calculate new width or height.

Here is a example of changing aspect.
We will make image height half.

.. literalinclude:: image_getsize_resize.py
   :language: python
   :linenos:
   :caption: image_getsize_resize.py

Here is an output.

.. figure:: image_getsize_resize.png
   :width: 600
   :class: with-border
   :align: center

   resize

Trimming
==========

If the image contains useless part, you can trim/crop it with method ``trim()``.

Implementing this for next release.


Flip Horizontally and Vertically
==================================

You can flip image easily.
``mirror()`` is used for horizontal flip.
And ``flip()`` is used for vertical flip.

.. literalinclude:: image_mirror_flip.py
   :language: python
   :linenos:
   :caption: image_mirror_flip.py

Here is an output.

.. figure:: image_mirror_flip.png
   :width: 600
   :class: with-border
   :align: center

Change color
==============

Drawlib provides lots of changing color function.
``grayscale()`` makes the image gray scale.
And ``sepia()`` makes the image sepia color.

.. literalinclude:: image_grayscale_sepia.py
   :language: python
   :linenos:
   :caption: image_grayscale_sepia.py

Here is an output.

.. figure:: image_grayscale_sepia.png
   :width: 600
   :class: with-border
   :align: center

``brightness()`` change brightness.
0.0 is complete dark and 1.0 is original. You can set values bigger than 1.0. It makes more light on the image.

.. literalinclude:: image_brightness.py
   :language: python
   :linenos:
   :caption: image_brightness.py

Here is an output.

.. figure:: image_brightness.png
   :width: 600
   :class: with-border
   :align: center

``invert()`` reverse RGB and ``colorize()`` put colors to grayscaled image.

.. literalinclude:: image_invert_colorize.py
   :language: python
   :linenos:
   :caption: image_invert_colorize.py

Here is an output.

.. figure:: image_invert_colorize.png
   :width: 600
   :class: with-border
   :align: center

``mosaic()`` apply mosaic effect.
It takes optional argument ``block_size``. It is a mosaic pixel size. Default is 8.
``blur()`` apply blur effect.

.. literalinclude:: image_mosaic_blur.py
   :language: python
   :linenos:
   :caption: image_mosaic_blur.py

Here is an output.

.. figure:: image_mosaic_blur.png
   :width: 600
   :class: with-border
   :align: center
