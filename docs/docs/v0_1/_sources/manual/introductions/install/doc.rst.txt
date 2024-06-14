===============
Install
===============

You can install drawlib with the following command. If your system uses ``python3`` and ``pip3``, use them instead.

.. code-block:: none

   $ pip install drawlib

After installation, you can check whether drawlib installed successfully or not through these commands.

.. code-block:: none

   $ python -m drawlib --version
   software=0.1.24
   api=0.1.24

   $ drawlib --version 
   software=0.1.24
   api=0.1.24

Drawlib package also install ``drawlib`` command which is useful for building many images.
It is calling drawlib libraries script which is equivalent to ``python -m drawlib``.
Please check details at that section at foundation chapter.

By the way, not only the software (library) version, you can also see the API version too.
This is because drawlib supports the old API (previously released library's API) in the new version for backward compatibility.
You can specify drawlib api version like this.

.. code-block:: none

   $ python -m drawlib.v0_1 --version
   software=0.1.24
   api=0.1.24

Installed successed but unable to run
---------------------------------------

Drawlib depends on ``matplotlib`` and it requires ``msvc-runtime`` on Windows.
If it is not automatically installed, you will see these kind of error when you draw.

.. code-block:: none

   ImportError: DLL load failed while importing _cext: The specified module could not be found

On that situation, please manually install ``msvc-runtime``.

.. code-block:: none

   pip install msvc-runtime

If you hit another error, please check python environment is too old or too latest.

Versioning 
===========

Drawlib follows the versioning rule ``<major>.<minor>.<patch>``. 

- Major Version: Significant API change
- Minor Version: Minor API change
- Patch Version: Bug fixes, etc. No API change

If you intend to use drawlib with a long-term project, we recommend installing a specific version with requirements.txt.

.. code-block:: none

   drawlib == 0.1.*
   sphinx == 7.2.*
   sphinx-rtd-theme == 2.0.*

And install/update them using it.

.. code-block:: none

   $ pip install -U -r requirements.txt

As you can see, the patch version is not specified. So bug fixes will be updated, but there will be no API change. 
We recommend not only specifying drawlib but also the version of the documentation building tool (sphinx, etc.).

Release policy
=================

Drawlib's release is as follows

* 0.1.* : private alpha release
* 0.2.* : public beta release
* 0.n.* : public releases
* n.m.* : matured public releases

After public release 0.3, each version have devepment releases. such as

* 0.3.0.dev1
* 0.3.0.dev2
* 0.3.0.dev<n>

As you can see, patch version is 0 and having ``dev<n>`` after that.
It is under-development testing releases for library developer and power users.
You can't install them via pip normally.
But able to install with specifying exact version. Like this.

.. code-block:: none

   $ pip install drawlib == 0.3.0.dev1

After this under-development phase ends, release official version such as "0.3.1".

After drawlib matured, we move to version "1.0.*" and later.
Here is a release plan image.

.. figure:: image1.png
    :width: 600
    :class: with-border
    :align: center

    image1.png

Unfortunately, we are not planning to publish older new fix version.
It means, after releasing version ``0.n.0``, we will not provide new patch release ``0.<n-1>.*``.

Virtual Environment
=====================

If you have many documentation projects on your machine, we recommend installing drawlib in a Python virtual environment, such as venv or poetry. 
We use venv for pure documentation projects and poetry for development projects with documentation.

By using them, you can use different drawlib versions for different projects and avoid underlying library version conflicts, such as matplotlib.
