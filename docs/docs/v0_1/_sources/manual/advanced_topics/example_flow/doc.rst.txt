===========================
Example of Doc Build Flow
===========================

Here is a high level documentation build frlow with drawlib.

.. figure:: ../../introductions/index/image3.png
    :width: 600
    :class: with-border
    :align: center

    Build many images

In this document, we will explain real world example and its procedure step by step.
The content is based on this documentation's build flow itself.
However, it is normalized to simlify the explanation.

Example GitHub Repository
==========================

We created example GitHub Repository which build documentation and publish it through GitHub pages.

https://github.com/yuichi110/drawlib_docs_example


What tool we use
==================

We will use these tools for writing and publishing doc.

- Drawlib: For building image
- Sphinx: For building docs with pre-build images
- GitHub Pages: Publish the document

We will write python doc in our scenario.
So, we choose ``Sphinx`` since it is popular.

Sphinx requires understanding reStructuredText.
In my opinion it is similar to markdown but less popular and more complex.
However the complexity make you free for difficulty of structuring doc pages to one documentation.
``Jekyll`` might be alternative option of Sphinx. It create documentation from markdown files.

Repository structure
=======================

Here is repository structure.

.. code-block:: none

   repository
   ├── .gitignore
   ├── .venv
   ├── LICENSE
   ├── README.md
   ├── requirements.txt
   ├── docs
   |   └── ...
   ├── scripts
   |   └── ...
   ├── source
   │   ├── __init__.py
   │   ├── _static
   │   ├── _templates
   │   ├── chapter01
   │   ├── chapter0
   │   ├── commons
   │   ├── conf.py
   │   ├── index
   │   └── index.rst
   └── staging
       └── ...

Documentation source is contained in ``/source``.
We build image first and then build docs at here.

Builded docs(HTML) are stored in ``/staging`` first.
As its name denotes, this is the directory for checking documentation.

After finding new document has no problem, move its content to ``/docs``.
This is a directory for GitHub pages publication.
Please be careful, GitHub page can publish its content at root level or ``/docs`` directory.

Directory ``/scripts`` contains many script files for building/checking/publishing.

Python Environment
======================

Building images and docs requires Python packages.
We will use virtual environment for avoiding package conflict etc.
Here is a bash script for creating environment.

.. code-block:: bash

   #!/bin/bash
   set -e

   # cd to repository root
   cd "$(dirname "$0")"
   cd ../

   # delete python venv
   deactivate || true
   rm -rf .venv

   # create venv and activate
   python -m venv .venv
   source .venv/bin/activate

   # install python packages
   pip install -U -r requirements.txt

At last, installing python packages from ``requirements.txt``.

.. code-block:: none

   drawlib == 0.1.*
   sphinx == 7.2.*
   sphinx-rtd-theme == 2.0.*

After issuing this script, python environment and its libraries are installed.
If sphinx configs are not ready, prepare them with ``sphinx`` commands.


Source Directory: source
=========================

Directory ``source`` contains sphinx project files and documentation source.
From point of drawlib, ``source`` is a root of your package.
Since it is python package, it has ``__init__.py``.

This directory contains many python files for illustration.
Such as 

- source/chapter01/section01/image.py
- source/chapter01/section02/image.py

Here is a code of ``/source/chapter01/section01/image.py``

.. code-block:: python

   from drawlib.apis import *

   import source.commons.style
   import source.commons.util as util

   config(width=100, height=50)
   util.draw_3rectangle(50, 25, 20, 15, 5)
   util.draw_logo()
   save()

As you can see, it imports ``source.commons`` package's modules.
They are style definition codes which we explain at previous document.

For building images, we use script ``/scripts/build_images.py``

.. code-block:: bash

   #!/bin/bash
   set -e

   # cd to project root directory
   cd "$(dirname "$0")"
   cd ../

   # activate
   source .venv/bin/activate

   # build
   drawlib ./source

It builds all images in source directory.
If the documentation project is large, we recommend creating build scripts per chapter or section.
We have ``scripts/build_images_chapter01.py`` and ``scripts/build_images_chapter02.py`` in our case.

.. code-block:: bash

   #!/bin/bash
   set -e

   # cd to project root directory
   cd "$(dirname "$0")"
   cd ../

   # activate
   source .venv/bin/activate

   # build
   drawlib ./source/chapter01

After confirming builded images are OK, we will build documentation with another script again.
``script/build_docs.sh`` do that.

.. code-block:: bash

   #!/bin/bash
   set -e

   # cd to project root directory
   cd "$(dirname "$0")"
   cd ../

   # activate
   source .venv/bin/activate

   # delete last build target contents
   rm -rf ./staging

   # build to html
   sphinx-build -a ./source ./staging

At the script, we delete old build file at first with ``rm -rf ./staging``.
And then, build docs normally with ``sphinx-build -a ./source ./staging``.

Build Output Directory: staging
=================================

Directory ``staging`` is just an sphinx build's output directory.
However, you need to check it before publishing.
Script ``scripts/serv_staging.sh`` start HTTP server which hosts this directory.
And then open browser automatically.

.. code-block:: bash

   #!/bin/bash
   set -e

   open_browser_1sec_later() {
      sleep 1
      open http://localhost
   }

   # cd to doc root
   cd "$(dirname "$0")"
   cd ../

   # activate
   source .venv/bin/activate

   # open browser later
   open_browser_1sec_later &

   # cd to html directory and start http server
   cd ./staging
   python -m http.server 80

GitHub Pages Directory: docs
======================================

After you confirmed staging contents has no problem.
It's time to publish the content.

If you haven't configured Github pages on your repository, please configure it first.
You can do it at settings/pages.

.. figure:: image_github_pages.png
   :width: 600
   :class: with-border
   :align: center

    Configure github pages

For moving files from ``staging`` to ``docs``, call script ``/scripts/deploy_from_staging_to_docs.sh``.

.. code-block:: bash

   #!/bin/bash
   set -e

   # cd to doc root
   cd "$(dirname "$0")"
   cd ../

   # delete old docs
   rm -rf ./docs

   # copy latest staging to docs
   cp -r ./staging ./docs

   # create .nojekyll
   cd ./docs
   touch .nojekyll

After moving HTML content, do ``git commit`` and ``git push``.
After remote repository is updated, GitHub pages will be also updated.
