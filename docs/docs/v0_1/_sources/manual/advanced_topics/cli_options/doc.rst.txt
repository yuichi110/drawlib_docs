=================
CLI and Options
=================

After you install drawlib via pip, you can use ``drawlib`` command.
The command is equivalent to calling drawlib module via ``python -m drawlib``.

There are big difference between ``python <your drawlib code>`` and ``drawlib <your drawlib code or directory>``.
Former one just call python program normally.
However, the latter call drawlib's special function first. And then it calls your codes.

When you call single file which doesn't import any of your another file, there are no big difference.
However, ``drawlib`` command do these thing before executing your code.

- Detect your package architecture and register path
- Call all python files which exsits under the target directory
- Able to enable auto apply ``clear()`` and ``dutil_canvas.initialize()`` before executing each files.

If you want to draw many illustrations, we strongly recommend using ``drawlib`` command rather than calling file via ``python``.

Options
=========

``drawlib`` command has ``-h`` option which shows command help.

.. code-block:: none
    $ drawlib -h
    usage: drawlib [-h] [-v] [--purge_font_cache] [--disable_auto_clear] [--enable_auto_initialize] [--quiet] [--verbose] [--developer] ...

    Ilustration as code by python

    positional arguments:
    file_or_directory     Target python file or directory which contains python codes

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         Show version.
    --purge_font_cache    Purge cached font files.
    --disable_auto_clear  Disable clearing canvas per executing drawing code files.
    --enable_auto_initialize
                            Enable initializing theme/canvas/image_cache per executing drawing code files.
    --quiet               Enable quiet logging. show only error messages
    --verbose             Enable verbose logging.
    --debug               Enable verbose logging. Equivalent to option "--verbose".
    --developer           Enable verbose logging. Disable error handling for library users.

Auto ``clear()`` is enabled by default.
You can disable it via ``--disable_auto_clear``.

``clear()`` doesn't wipe theme settings and image cache.
They should be keep normally since many user want to apply same theme to many illustration codes.
However, if you want to completely initialize drawlib per illustration code, you can use option ``--enable_auto_initialize``.
It will make drawlib call ``dutil_canvas.initialize()`` every time when drawlib execute your code files.

``--purge_font_cache`` option remove drawlib's font file cache from your local machine.
Font file is downloaded when you use the font first time and it is cached.
This purge option delete them and release disk space.
Normally, sum of font file size is less than 100MB.
Using Chinese Japanese font tends to use more space since they posses lots of characters.
Uninstalling drawlib will also delete fonts too since drawlib make font file caches in its library directory.

Option ``--quiet``, ``--verbose``, ``--debug``, ``--developer`` will change log level.
If you hit trouble and want to investigate detail error, please use ``--verbose`` and ``--debug``.
If you good at Python, ``--developer`` option might give you more detail error.
