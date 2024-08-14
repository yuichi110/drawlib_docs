=======================
Release Note of 0.2.*
=======================

Version 0.2.3 
================

Release data: 2024/08/13
--------------------------

Commit: `fa1d90a <https://github.com/yuichi110/drawlib/commit/fa1d90a4a45fb3edab2cbafddfa04ef23d6a5691>`_
-----------------------------------------------------------------------------------------------------------

New features
--------------

Adding shape arrow functions.

- ``arrow_polyline()``
- ``arrow_l()``
- ``arrow_u()``
- ``arrow_arc()``

Adding smart arts.

- ``dsart.BoxList``
- ``dsart.BulletPoints``
- ``dsart.GridLayout``
- ``dsart.Pyramid``
- ``dsart.Table``
- ``dsart.Tree``

Adding style model attribute.

- ``ShapeTextStyle.xy_abs_shift``


Breaking changes
-------------------

Change arg names 

- From ``from_angle`` to ``angle_start``
- From ``to_angle`` to ``angle_end``

At these functions.

- ``arc()``
- ``fan()``
- ``wedge()``

Change arg names at function ``dsart.bubblespeech()``.

- From ``tail_from_ratio`` to ``tail_start_ratio``
- From ``tail_to_ratio`` to ``tail_end_ratio``

0.2.2
=====================

Release data: 2024/07/02
--------------------------

Commit: `fa1d90a <https://github.com/yuichi110/drawlib/commit/fa1d90a4a45fb3edab2cbafddfa04ef23d6a5691>`_
-----------------------------------------------------------------------------------------------------------

First release of Drawlib ``0.2``.