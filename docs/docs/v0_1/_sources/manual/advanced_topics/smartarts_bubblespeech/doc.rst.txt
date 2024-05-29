==========================
Smart Arts: Bubblespeech
==========================

Bubble Speech is not regular shape but it is used on illustrations some times.
It is implemented in smart art function ``dsart.``.
You can consider bubble speech as oee of complex shape functions.

.. literalinclude:: image1.py
   :language: python
   :linenos:
   :caption: image1.py

We can draw source code like this.

.. figure:: image1.png
    :width: 600
    :class: with-border
    :align: center

    image1.png

Options are little bit complex, but the key point is how to draw tail.
Except tail, bubble speech is almost rectangle which can use only align left, bottom.

- xy: always left, bottom.
- tail_edge: which edge tail exist. one of ``left``, ``right``, ``bottom``, ``top``
- tail_from_ratio: where tail start. 0.0 ~ 1.0. start point is bottom(edge is left or right) and left(edge is bottom or top)
- tail_vertex_xy: tail vertex location
- tail_to_ratio: where tail end. 0.0 ~ 1.0. It must be bigger than ``tail_from_ratio``.

OK, let's check those options at image picture.

.. figure:: image2.png
    :width: 600
    :class: with-border
    :align: center

    image2.png