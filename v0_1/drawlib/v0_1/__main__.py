# Copyright (c) 2024 Yuichi Ito (yuichi@yuichi.com)
#
# This software is licensed under the Apache License, Version 2.0.
# For more information, please visit: https://github.com/yuichi110/drawlib
#
# This software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.

"""Entry point of ``drawlib.v0_1``

When you run ``python -m drawlib.v0_1 <options>``, this module is called.
And then, drawlib.v0_1.command.call() will be called.

"""

from drawlib.v0_1.private.command import call

if __name__ == "__main__":
    call()