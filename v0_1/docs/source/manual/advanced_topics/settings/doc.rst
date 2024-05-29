===================
Library Settings
===================

Drawlib provides ``dsettings`` object.
It posses few functions for changing library settings.
Here are the function.

- ``get_logging_mode()``
- ``set_logging_mode(mode: str)``
- ``get_suppress_warning()``
- ``set_suppress_warning(enable: bool)``
- ``is_debug_mode()``
- ``is_developer_debug_mode()``

Currently, settings are related to only logging level and its behavior.

Logging
==========

Drawlib can change log level.
But log level doesn't mean syslog's one.
But drawlib's level.

- ``quiet``: show only warning and error. Equivalent to logging.ERROR
- ``normal``: default. Equivalent to logging.INFO
- ``verbose``: many log. Equivalent to logging.DEBUG
- ``developer``: verbose option + disabling error handling.

You can set level via ``set_logging_mode(mode)``.
And able to get current level via ``get_logging_mode()``.

Suppressing Warnings
========================

Error Handler and Logging Mode
=================================