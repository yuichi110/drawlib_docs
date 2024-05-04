=========================
drawlib for writing docs
=========================

Many documentation requires illustration images.
Documentation text is managed by version control system especially Git normally.
However illustration images aren't since they are binary files.

That is the reason why this library is developed.
Drawlib draw illustration via python script easily.
Git able to manage python code, it means Git can manage drawlib's illustration code too.
We achieve illustration as code for documentation in this logic.

In this documentation, we will let you know how drawlib manage and build its own documetation which has lots of images.
You might be able to get insight for how to achieve managing your documetation with images by reading this doc.
Writing books are almost same to writing docs.

What tool we use
==================

drawlib docs has 2 part.

- manual (hand writing documentation)
- apidoc (automatically generated from code)

We use ``Sphinx`` and ``reStructuredText`` for both of them.
You can use markdown if size of documentation is small, but I recommend using reStructuredText for large documentation since it has many feature for organizing files as 1 documentation.

However, Sphinx can take care making doc from text files only.
It doesn't handle image creation of course.
Yes, ``drawlib`` does it in our doc creation process. 

Documentation creation process
=================================

Our documentation has 2 part as we noted.
Hand writing manual and automatically generated API docs.
Manual contains lots of images.

To create documentation which has image/manual/api-docs, we build our docs in this procedure.

1. build image first at documentation ``source`` directory which contains ``source/index.rst`` and ``source/manual``.
2. copy doc source to ``merged/manual`` directory after deleting old existing files
3. run ``sphinx-apidoc`` and generate api docs to ``merged/api``
4. run ``sphinx-build`` at ``merged`` directory and export html to ``html`` directory.

all of them exist under ``docs_workspace``.
After we confirm generated docs under ``html`` is OK, copy it to ``docs/<version>`` directory.
The ``docs`` directory is published to internet through GitHub Pages.
Since we need to publish old version documentation, it has version hierarchy.

We do these build procedure by bash script.
But publication is handled manually. Since it is dangerous and easy (just copy paste and Git push).
We will share build script later.

Directory structure of workspace
===================================

Workspace for creating documentation has this hierarchy

.. code-block:: none

   docs_workspace ---+--- source ---+--- index.rst
                     |              +--- <images codes which index.rst uses>
                     |              +--- <image files which are generated from codes>
                     |              |
                     |              +--- .drawlib ---+--- docstyles.py
                     |              |                +--- docimages.py
                     |              |                +--- image icon files for cache
                     |              |                +--- text fonts for cache
                     |              |
                     |              +--- manual ---+--- About -----+--- doc.rst
                     |                             |               +--- <image's codes>
                     |                             |               +--- <image files>
                     |                             |
                     |                             +--- Install ---+--- doc.rst
                     |                             |               +--- <images codes>
                     |                             |               +--- <image files>
                     |                             .
                     |                             .
                     |
                     +--- merged ---+--- index.rst
                     |              +--- image files 
                     |              |
                     |              +--- manual ---+--- About -----+--- doc.rst
                     |              |              |               +--- <image's codes>
                     |              |              |               +--- <image files>
                     |              |              |
                     |              |              +--- Install ---+--- doc.rst
                     |              |              |               +--- <image's codes>
                     |              |              .               +--- <image files>
                     |              |              .
                     |              |
                     |              +--- api --- <generated files>
                     |
                     +--- html --- <generated files>

We don't touch ``doc_workspace/merged`` and ``doc_workspace/html`` since they are just export point of sphinx commands.
We write manual at ``doc_workspace/source`` only.

As you can see ``source`` contains ``index.rst``.
It becomes top page of this document.
Since we use ``Sphinx`` and ``reStructuredText``, this index has ``toctree``.
Other file can have toctree of course. But we are avoiding it.
On same directory, we put drawlib's python scripts for creating images which ``index.rst`` uses.

In this directory, we have ``.drawlib`` directory too.
We define common line/shape/text styles at here for achiving applying same styles to all images.
Creating images at each file is not recommended since having diffuculty for change and keep governance.
Also, we prepare common icons which are used in each images.

Each documentation page has its own directory.
Such as ``About`` and ``Install``.
They have documentation text(``doc.rst``) and its images and the codes which generate them.

In summary, we are keeping this rule

- 1 directory contains all 1 page contents
- index.rst connects all pages
- .drawlib provides common style and icons to all image codes.

sphinx conf.py
================

.. literalinclude:: ../../conf.py
   :language: python
   :caption: run_build_docs.sh


Build script
=================

We put scripts under ``scripts`` directory.

.. literalinclude:: ../../../../scripts/run_build_docs.sh
   :language: bash
   :caption: run_build_docs.sh

We can't assure where the script is called.
So, we first change directory to script directory via ``cd "$(dirname "$0")"`` and then move to project root via ``cd ../``.
After that, script main part will start.

As we told in procedure part, it does

1. build images via ``poetry run python -m drawlib ./docs_workspace/source``
2. delete old files via ``rm -rf ./docs_workspace/merged``
3. then copy image via ``rsync`` command. We don't use ``cp`` command since rsync can exclude python files easily.
4. copy important but excluded file manually via ``cp ./docs_workspace/source/conf.py ./docs_workspace/merged/``
5. generate api doc via ``poetry run sphinx-apidoc -f -o ./docs_workspace/merged/api ./drawlib``
6. build to html via ``run sphinx-build -a ./docs_workspace/merged ./docs_workspace/html``

That's all!!

For checking html, we use this utility script too.
Which run HTML server on the HTML directory and open browser.

.. literalinclude:: ../../../../scripts/run_server_docs.sh
   :language: bash
   :caption: run_server_docs.sh