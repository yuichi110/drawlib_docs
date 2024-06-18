======================
Building many images
======================

Drawlib is designed for creating lots of illust for ducumentation etc.
Here is a typical build process.

.. figure:: ../../introductions/index/image3.png
    :width: 600
    :class: with-border
    :align: center

    Build many images

As you can see you can achieve

- declare styling at common code files
- declare functions at common code files
- each image codes import them
- execute all image codes under specified directory and generate images

For building many images, you should remember these 2 topics.

- Create normal python package architecture
- don't forget create ``__init__.py`` on each directories.
- Call drawlib module via python ``python -m drawlib <directory_name>``

We will cover them one by one.
Here is a sample project architecture.

.. code-block:: none

   docs
   ├── __init__.py
   ├── chap01
   │   ├── __init__.py
   │   ├── image1.py
   │   ├── image2.py
   ├── chap02
   │   ├── __init__.py
   │   └── image1.py
   └── commons
      ├── __init__.py
      ├── avenger
      │   ├── readme.txt
      │   └── regular.ttf
      ├── images
      │   ├── linux.png
      │   └── python.png
      ├── style.py
      └── util.py

``docs`` is root directory of documents.
``commons`` contains codes which are used by image codes. And also it contains files (in this case font and image) which are used by common codes.
``chap01`` contains image codes. Document text code such as Markdown might be put on this directory in real world.
``chap02`` is almost same to chap01. Both chap01 and chap02 has same name code file ``image1.py``. It is OK since directory is different.

Create Drawing Project as Python Package
===========================================

Image code's depends on common codes.
Such as styling and utility.
The word "depends" means ``import`` or ``from import`` at python.
So, image codes import common codes.

In small project, you can adopt flat directory.
It means all files are in one directory.
However, putting few hundreads of image code in to one directory is not smart.
You should separate directories fitch fit to document architecture.

On that time, python code need to import code which exsits on another directory.
Which requires creating package architecture.
And use it for import module name.

Here is a sample code.

.. literalinclude:: ../../../../../samples/build_many/docs/chap01/image1.py
   :language: python
   :linenos:
   :caption: docs/chap01/image1.py

As you can see, it imports ``style.py`` and ``util.py``.
The module name has parent directories from the root.
This style is called ``Absolute import``.
We recommend usint this style.
But you can use another import method ``Relative import`` too.

Please be careful all directories which has python code posses ``__init__.py``.
``__init__.py`` is important for python's package system.
If it exists, the directory becomes package.
Newer python doesn't rely on it, but putting it is good for declaration.
If you wants you can write code to it.

Drawlib checks which directory posses ``__init__.py``.
And all directory which posses python file of having child directory which posses python file requires to have ``__init__.py``.
So, 

- docs: ``__init__.py`` exist. Having no python files as its child, but child directory posses them.
- docs.chap01 etc: ``__init__.py`` exist.
- docs.commons.images: There are no ``__init__.py`` since it doesn't have python file. You can put ``__init__.py`` if you wants.

In this case, ``docs`` is package root since its parent directory doesn't posses ``__init__.py``.
If parent directory has ``__init__.py``, it becomes root package.

Python Path
===============

Python path is a list of directories which python search modules.
You can check it via ``sys.path``.

.. code-block:: none

   $ python
   Python 3.9.19 (main, May  1 2024, 23:01:19)
   [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import sys
   >>> import pprint
   >>> pprint.pprint(sys.path)
   ['',
   '/Users/yuichi/.pyenv/versions/3.9.19/lib/python39.zip',
   '/Users/yuichi/.pyenv/versions/3.9.19/lib/python3.9',
   '/Users/yuichi/.pyenv/versions/3.9.19/lib/python3.9/lib-dynload',
   '/Users/yuichi/.pyenv/versions/3.9.19/lib/python3.9/site-packages']

When you try to import packages and modules in your code, python search them from these locations.
Python path posses

- Current working directory
- Where python is installed
- Directory which has external packages which you install via pip etc

When you call drawlib with special manner, drawlib add your package to Python Path.
So, you can any code which is inside of your package

python -m drawlib <directory or code>
=========================================

Normmaly, you can call package entry point (``main.py`` or ``__main__.py``).
But unable to call each inside packages which depends on package.
Let's try calling ``docs.chap1.image1.py`` normally.

.. code-block:: none

   $ python docs/source/docs/chap01/image1.py 
   Traceback (most recent call last):
   File "/Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/chap01/image1.py", line 3, in <module>
      import docs.commons.style
   ModuleNotFoundError: No module named 'docs'

It shows error as we told.
The error message says python can't find package ``docs``.

Drawlib can call any code in your package without complicated procedure.
Just use ``python -m drawlib <target>``.
Let's try.

.. code-block:: none

   $ python -m drawlib docs/source/docs/chap01/image1.py
   Detect package root "/Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs".
      - Add parent directory of package root "/Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source" to Python Path.

   Execute python files
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/chap01/image1.py

As the console shows, it detects package root and register it to python path first.
After that, python can use your package anywhere since it is path.
Then, calling inside code success.

This command is able to call directory.
When directory is specified, all python codes are executed onece.
It is normal python behavior. 2nd time calling is not executed but getting module cache.

.. code-block:: none

   $ python -m drawlib docs/source/docs                 
   Detect package root "/Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs".
      - Add parent directory of package root "/Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source" to Python Path.

   Execute python files
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/__init__.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/chap02/image1.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/chap02/__init__.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/commons/style.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/commons/util.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/commons/__init__.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/chap01/image1.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/chap01/__init__.py
      - /Users/yuichi/GitHub/drawlib_docs/v0_1/docs/source/docs/chap01/image2.py

In summary, you need to remember these simple rules for building many images.

- Create package structure
- All directories in your package must have ``__init__.py``
- Parent directory of your package must not have ``__init__.py``
- Execute python codes via ``python -m drawlib <target>`` command

Sample Codes and Its Outputs
===============================


.. literalinclude:: ../../../../../samples/build_many/docs/commons/style.py
   :language: python
   :linenos:
   :caption: docs/commons/style.py

.. literalinclude:: ../../../../../samples/build_many/docs/commons/util.py
   :language: python
   :linenos:
   :caption: docs/commons/util.py

.. literalinclude:: ../../../../../samples/build_many/docs/chap01/image1.py
   :language: python
   :linenos:
   :caption: docs/chap01/image1.py

.. figure:: ../../../../../samples/build_many/docs/chap01/image1.png
    :width: 600
    :class: with-border
    :align: center

    output image of docs/chap01/image1.py

.. literalinclude:: ../../../../../samples/build_many/docs/chap01/image2.py
   :language: python
   :linenos:
   :caption: docs/chap01/image2.py

.. figure:: ../../../../../samples/build_many/docs/chap01/image2.png
    :width: 600
    :class: with-border
    :align: center

    output image of docs/chap01/image2.py

.. literalinclude:: ../../../../../samples/build_many/docs/chap02/image1.py
   :language: python
   :linenos:
   :caption: docs/chap02/image1.py

.. figure:: ../../../../../samples/build_many/docs/chap02/image1.png
    :width: 600
    :class: with-border
    :align: center

    output image of doc/schap02/image1.py