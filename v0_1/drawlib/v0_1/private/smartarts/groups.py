# Copyright (c) 2024 Yuichi Ito (yuichi@yuichi.com)
#
# This software is licensed under the Apache License, Version 2.0.
# For more information, please visit: https://github.com/yuichi110/drawlib
#
# This software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.


class Groups:
    def __init__(self): ...

    def render(self): ...

    def set_default_style(self, textstyle, shapestyle): ...

    def append_group(self, group_name, shapestyle): ...

    def append_group_member(self, group_name, shapestyle): ...
