===================
Debugging errors
===================

Drawlib hide detail error when user code makes trouble.
On that time drawlib shows only

- Which file and line has problem
- What error happens

It means drawlib doesn't show stucktrace and where library code makes error from user input.
It is because we believe showing detail error and inside of drawlib is not good for ordinary users.

However, some times you want to check details.
On that situation you need to enable debug mode.

How to enable debug mode
============================

Drawlib controlls which output is shown on cosole via logging level.
Detail of error log is shown only on debug level logging.

To set logging level debug, you have 2 options.

- Set logging level via calling function: ``dsettings.set_logging_mode("debug")``
- Set logging level via CLI Option ``python -m drawlib --quiet/--verbose/--developer``

Please check details on settings doc and CLI options docs for details.
