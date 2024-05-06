===============
Install
===============

You can install drawlib with the following command. If your system uses ``python3`` and ``pip3``, use them instead.

.. code-block:: none

   $ pip install drawlib

After installation, you can check the version with this command.

.. code-block:: none

   $ python -m drawlib --version
   software=0.1.1
   api=0.1.1

Not only the software (library) version, but you can also see the API version too.
This is because drawlib supports the old API (previously released library's API) in the new version for backward compatibility.

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

Virtual Environment
=====================

If you have many documentation projects on your machine, we recommend installing drawlib in a Python virtual environment, such as venv or poetry. 
We use venv for pure documentation projects and poetry for development projects with documentation.

By using them, you can use different drawlib versions for different projects and avoid underlying library version conflicts, such as matplotlib.
