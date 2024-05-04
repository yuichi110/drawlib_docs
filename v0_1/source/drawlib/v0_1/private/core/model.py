# Copyright (c) 2024 Yuichi Ito (yuichi@yuichi.com)
#
# This software is licensed under the Apache License, Version 2.0.
# For more information, please visit: https://github.com/yuichi110/drawlib
#
# This software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.

"""Wrapper of matplotlib drawing object style

This module contains drawlib's style classes.
They provide consistent style setting ways for line/text/shapes.

"""

# pylint: disable=too-many-instance-attributes


#
# Please don't use external data classes such as pydantic.
# Use property for validation
#

import dataclasses
from typing import (
    Union,
    Optional,
    Tuple,
    Literal,
    Final,
)
from drawlib.v0_1.private.core.fonts import (
    Font,
    FontArabic,
    FontBase,
    FontSerif,
    FontSanSerif,
    FontChinese,
    FontJapanese,
    FontKorean,
    FontMonoSpace,
    FontRoboto,
    FontSourceCode,
    FontFile,
)
from drawlib.v0_1.private.core.model_validator import (
    ColorValidator,
    AlignValidator,
    LineValidator,
    TextValidator,
    CoordinateValidator,
)
from drawlib.v0_1.private.core.colors import Colors


class IconStyleDefault:
    """default value of IconStyle."""

    style: Final[str] = "thin"
    color: Final[Tuple[int, int, int]] = Colors.Black
    alpha: Final[None] = None
    haligh: Final[str] = "center"
    valign: Final[str] = "center"


@dataclasses.dataclass
class IconStyle:
    """drawlib image style dataclass."""

    style: Optional[Literal["thin", "light", "regular", "bold", "fill"]] = None
    color: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
    alpha: Optional[float] = None
    halign: Optional[Literal["left", "center", "right"]] = None
    valign: Optional[Literal["bottom", "center", "top"]] = None

    @property  # type: ignore[no-redef]
    def style(self) -> Optional[str]:
        """getter of style"""
        return getattr(self, "_style", None)

    @style.setter
    def style(self, value: Optional[str]) -> None:
        """setter of style"""
        if isinstance(value, property) or value is None:
            self._style = None
            return

        if value not in ["thin", "light", "regular", "bold", "fill"]:
            raise ValueError(f'IconStyle.style does not support "{value}".')
        self._style = value

    @property  # type: ignore[no-redef]
    def color(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of color"""
        return self._color

    @color.setter
    def color(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of style"""
        if isinstance(value, property) or value is None:
            self._color = None
            return

        ColorValidator.validate_color(value)
        self._color = value

    @property  # type: ignore[no-redef]
    def alpha(self) -> Optional[float]:
        """getter of alpha"""
        return self._alpha

    @alpha.setter
    def alpha(self, value: Optional[float]) -> None:
        """setter of alpha"""
        if isinstance(value, property) or value is None:
            self._alpha = None
            return

        ColorValidator.validate_alpha(value)
        self._alpha = value

    @property  # type: ignore[no-redef]
    def halign(self) -> Optional[str]:
        """getter of halign"""
        return self._halign

    @halign.setter
    def halign(self, value: Optional[Literal["left", "center", "right"]]) -> None:
        """setter of halign"""
        if isinstance(value, property) or value is None:
            self._halign = None
            return

        AlignValidator.validate_halign(value)
        self._halign = value

    @property  # type: ignore[no-redef]
    def valign(self) -> Optional[str]:
        """getter of valign"""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[Literal["bottom", "center", "top"]]) -> None:
        """setter of valign"""
        if isinstance(value, property) or value is None:
            self._valign = None
            return

        AlignValidator.validate_valign(value)
        self._valign = value


class ImageStyleDefault:
    lstyle: Final[str] = "thin"
    lcolor: Final[Tuple[int, int, int]] = Colors.Black
    lwidth: Final[float] = 0
    halign: Final[str] = "center"
    valign: Final[str] = "center"


@dataclasses.dataclass
class ImageStyle:
    """drawlib image style dataclass."""

    halign: Optional[Literal["left", "center", "right"]] = None
    valign: Optional[Literal["bottom", "center", "top"]] = None
    lwidth: Optional[float] = None
    lstyle: Optional[Literal["solid", "dashed", "dotted", "dashdot"]] = None
    lcolor: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None

    @property  # type: ignore[no-redef]
    def halign(self) -> Optional[str]:
        """getter of halign"""
        return self._halign

    @halign.setter
    def halign(self, value: Optional[Literal["left", "center", "right"]]) -> None:
        """setter of halign"""
        if isinstance(value, property) or value is None:
            self._halign = None
            return

        AlignValidator.validate_halign(value)
        self._halign = value

    @property  # type: ignore[no-redef]
    def valign(self) -> Optional[str]:
        """getter of valign"""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[Literal["bottom", "center", "top"]]) -> None:
        """setter of valign"""
        if isinstance(value, property) or value is None:
            self._valign = None
            return

        AlignValidator.validate_valign(value)
        self._valign = value

    @property  # type: ignore[no-redef]
    def lwidth(self) -> Optional[float]:
        """getter of lwidth"""
        return self._lwidth

    @lwidth.setter
    def lwidth(self, value: Optional[float]) -> None:
        """setter of lwidth"""
        if isinstance(value, property) or value is None:
            self._lwidth = None
            return

        LineValidator.validate_width(value)
        self._lwidth = value

    @property  # type: ignore[no-redef]
    def lstyle(self) -> Optional[str]:
        """getter of lstyle"""
        return self._lstyle

    @lstyle.setter
    def lstyle(self, value: Optional[str]) -> None:
        """setter of lstyle"""
        if isinstance(value, property) or value is None:
            self._lstyle = None
            return

        LineValidator.validate_style(value)
        self._lstyle = value

    @property  # type: ignore[no-redef]
    def lcolor(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of lcolor"""
        return self._lcolor

    @lcolor.setter
    def lcolor(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of lcolor"""
        if isinstance(value, property) or value is None:
            self._lcolor = None
            return

        ColorValidator.validate_color(value)
        self._lcolor = value


class LineStyleDefault:
    width: Final[float] = 1.0
    style: Final[str] = "solid"
    color: Final[Tuple[int, int, int]] = Colors.Black
    alpha: Final[None] = None


@dataclasses.dataclass
class LineStyle:
    """drawlib line style dataclass.

    Instead of providing lots of style parameters to drawing line
    functions ``line()`` etc,
    user set line style to line this way.

    1. Provide line style settings to ``LineStyle``.
    2. Provide the style instance to functions which uses line style.
    3. Line style is applied to drawn lines.

    It is easy for managing line styles and applying them to lots of texts.

    Note:
        Line style of shapes are configured at ``ShapeStyle``.

    """

    width: Optional[float] = None
    style: Optional[Literal["solid", "dashed", "dotted", "dashdot"]] = None
    color: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
    alpha: Optional[None] = None

    @property  # type: ignore[no-redef]
    def width(self) -> Optional[float]:
        """getter of width"""
        return self._width

    @width.setter
    def width(self, value: Optional[float]) -> None:
        """setter of style"""
        if isinstance(value, property) or value is None:
            self._width = None
            return

        LineValidator.validate_width(value)
        self._width = value

    @property  # type: ignore[no-redef]
    def style(self) -> Optional[str]:
        """getter of style"""
        return self._style

    @style.setter
    def style(self, value: Optional[str]) -> None:
        """setter of style"""
        if isinstance(value, property) or value is None:
            self._style = None
            return

        LineValidator.validate_style(value)
        self._style = value

    @property  # type: ignore[no-redef]
    def color(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of color"""
        return self._color

    @color.setter
    def color(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of color"""
        if isinstance(value, property) or value is None:
            self._color = None
            return

        ColorValidator.validate_color(value)
        self._color = value

    @property  # type: ignore[no-redef]
    def alpha(self) -> Optional[float]:
        """getter of alpha"""
        return self._alpha

    @alpha.setter
    def alpha(self, value: Optional[float]) -> None:
        """setter of alpha"""
        if isinstance(value, property) or value is None:
            self._alpha = None
            return

        ColorValidator.validate_alpha(value)
        self._alpha = value


class LineArrowStyleDefault:
    lwidth: Final[float] = 1.0
    lstyle: Final[str] = "solid"
    hstyle: Final[str] = "->"
    hscale: Final[float] = 20.0
    color: Final[Tuple[int, int, int]] = Colors.Black
    alpha: Final[None] = None


@dataclasses.dataclass
class LineArrowStyle:
    """drawlib line style dataclass.

    Instead of providing lots of style parameters to drawing line
    functions ``line()`` etc,
    user set line style to line this way.

    1. Provide line style settings to ``LineStyle``.
    2. Provide the style instance to functions which uses line style.
    3. Line style is applied to drawn lines.

    It is easy for managing line styles and applying them to lots of texts.

    Note:
        Line style of shapes are configured at ``ShapeStyle``.

    """

    lstyle: Optional[Literal["solid", "dashed", "dotted", "dashdot"]] = None
    lwidth: Optional[float] = None
    hstyle: Optional[Literal["->", "<-", "<->", "-|>", "<|-", "<|-|>"]] = None
    hscale: Optional[int] = None
    color: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
    alpha: Optional[float] = None

    @property  # type: ignore[no-redef]
    def lwidth(self) -> Optional[float]:
        """getter of lwidth"""
        return self._lwidth

    @lwidth.setter
    def lwidth(self, value: Optional[float]) -> None:
        """setter of lwidth"""
        if isinstance(value, property) or value is None:
            self._lwidth = None
            return

        LineValidator.validate_width(value)
        self._lwidth = value

    @property  # type: ignore[no-redef]
    def lstyle(self) -> Optional[str]:
        """getter of lstyle"""
        return self._lstyle

    @lstyle.setter
    def lstyle(self, value: Optional[str]) -> None:
        """setter of lstyle"""
        if isinstance(value, property) or value is None:
            self._lstyle = None
            return

        LineValidator.validate_style(value)
        self._lstyle = value

    @property  # type: ignore[no-redef]
    def hscale(self) -> Optional[float]:
        """getter of hscale"""
        return self._hscale

    @hscale.setter
    def hscale(self, value: Optional[float]) -> None:
        """setter of hscale"""
        if isinstance(value, property) or value is None:
            self._hscale = None
            return

        LineValidator.validate_arrowhead_scale(value)
        self._hscale = value

    @property  # type: ignore[no-redef]
    def hstyle(self) -> Optional[str]:
        """getter of hstyle"""
        return self._hstyle

    @hstyle.setter
    def hstyle(self, value: Optional[str]) -> None:
        """setter of lstyle"""
        if isinstance(value, property) or value is None:
            self._hstyle = None
            return

        LineValidator.validate_arrowhead_style(value)
        self._hstyle = value

    @property  # type: ignore[no-redef]
    def color(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of color"""
        return self._color

    @color.setter
    def color(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of color"""
        if isinstance(value, property) or value is None:
            self._color = None
            return

        ColorValidator.validate_color(value)
        self._color = value

    @property  # type: ignore[no-redef]
    def alpha(self) -> Optional[float]:
        """getter of alpha"""
        return self._alpha

    @alpha.setter
    def alpha(self, value: Optional[float]) -> None:
        """setter of alpha"""
        if isinstance(value, property) or value is None:
            self._alpha = None
            return

        ColorValidator.validate_alpha(value)
        self._alpha = value


class ShapeStyleDefault:
    halign: Final[str] = "center"
    valign: Final[str] = "center"
    lwidth: Final[float] = 1.0
    lstyle: Final[str] = "solid"
    lcolor: Final[Tuple[int, int, int]] = Colors.Black
    fcolor: Final[Tuple[int, int, int]] = Colors.White
    alpha: Final[None] = None


@dataclasses.dataclass
class ShapeStyle:
    """drawlib shape style dataclass.

    Instead of providing lots of style parameters to drawing shape
    functions ``circle()`` etc,
    user set shape style to shape this way.

    1. Provide text style settings to ``ShapeStyle``.
    2. Provide the style instance to functions which use shape style.
    3. Text style is applied to drawn shape.

    It is easy for managing shape styles and applying them to lots of shapes.

    Note:
        Line style of shapes are also configured on ShapeStyle too.
        LineStyle is not used.

    """

    halign: Optional[Literal["left", "center", "right"]] = None
    valign: Optional[Literal["bottom", "center", "top"]] = None
    alpha: Optional[float] = None
    lwidth: Optional[float] = None
    lcolor: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
    lstyle: Optional[Literal["solid", "dashed", "dotted", "dashdot"]] = None
    fcolor: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None

    @property  # type: ignore[no-redef]
    def halign(self) -> Optional[str]:
        """getter of halign"""
        return self._halign

    @halign.setter
    def halign(self, value: Optional[Literal["left", "center", "right"]]) -> None:
        """setter of halign"""
        if isinstance(value, property) or value is None:
            self._halign = None
            return

        AlignValidator.validate_halign(value)
        self._halign = value

    @property  # type: ignore[no-redef]
    def valign(self) -> Optional[str]:
        """getter of valign"""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[Literal["bottom", "center", "top"]]) -> None:
        """setter of valign"""
        if isinstance(value, property) or value is None:
            self._valign = None
            return

        AlignValidator.validate_valign(value)
        self._valign = value

    @property  # type: ignore[no-redef]
    def alpha(self) -> Optional[float]:
        """getter of alpha"""
        return self._alpha

    @alpha.setter
    def alpha(self, value: Optional[float]) -> None:
        """setter of alpha"""
        if isinstance(value, property) or value is None:
            self._alpha = None
            return

        ColorValidator.validate_alpha(value)
        self._alpha = value

    @property  # type: ignore[no-redef]
    def lwidth(self) -> Optional[float]:
        """getter of lwidth"""
        return self._lwidth

    @lwidth.setter
    def lwidth(self, value: Optional[float]) -> None:
        """setter of lwidth"""
        if isinstance(value, property) or value is None:
            self._lwidth = None
            return

        LineValidator.validate_width(value)
        self._lwidth = value

    @property  # type: ignore[no-redef]
    def lstyle(self) -> Optional[str]:
        """getter of lstyle"""
        return self._lstyle

    @lstyle.setter
    def lstyle(self, value: Optional[str]) -> None:
        """setter of lstyle"""
        if isinstance(value, property) or value is None:
            self._lstyle = None
            return

        LineValidator.validate_style(value)
        self._lstyle = value

    @property  # type: ignore[no-redef]
    def lcolor(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of lcolor"""
        return self._lcolor

    @lcolor.setter
    def lcolor(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of lcolor"""
        if isinstance(value, property) or value is None:
            self._lcolor = None
            return

        ColorValidator.validate_color(value)
        self._lcolor = value

    @property  # type: ignore[no-redef]
    def fcolor(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of fcolor"""
        return self._fcolor

    @fcolor.setter
    def fcolor(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of fcolor"""
        if isinstance(value, property) or value is None:
            self._fcolor = None
            return

        ColorValidator.validate_color(value)
        self._fcolor = value


class ShapeTextStyleDefault:
    alpha: Final[None] = None
    color: Final[Tuple[int, int, int]] = Colors.Black
    size: Final[float] = 16
    halign: Final[str] = "center"
    valign: Final[str] = "center"
    font: Final[Font] = Font.SANSSERIF_REGULAR
    angle: Final[None] = None
    flip: Final[bool] = False
    xy_shift: Final[None] = None


@dataclasses.dataclass
class ShapeTextStyle:
    """drawlib text style dataclass.

    Instead of providing lots of style parameters to drawing text
    functions ``text()`` etc,
    user set text style to text this way.

    1. Provide text style settings to ``TextStyle``.
    2. Provide the style instance to functions which uses text style.
    3. Text style is applied to drawn text.

    It is easy for managing text styles and applying them to lots of texts.

    """

    alpha: Optional[float] = None
    color: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
    size: Union[float, str, None] = None
    halign: Optional[Literal["left", "center", "right"]] = None
    valign: Optional[Literal["bottom", "center", "top"]] = None
    font: Union[
        Font,
        FontArabic,
        FontBase,
        FontSerif,
        FontSanSerif,
        FontChinese,
        FontJapanese,
        FontKorean,
        FontMonoSpace,
        FontRoboto,
        FontSourceCode,
        FontFile,
        None,
    ] = None
    angle: Optional[float] = None
    flip: Optional[bool] = None
    xy_shift: Optional[Tuple[float, float]] = None

    @property  # type: ignore[no-redef]
    def halign(self) -> Optional[str]:
        """getter of halign"""
        return self._halign

    @halign.setter
    def halign(self, value: Optional[Literal["left", "center", "right"]]) -> None:
        """setter of halign"""
        if isinstance(value, property) or value is None:
            self._halign = None
            return

        AlignValidator.validate_halign(value)
        self._halign = value

    @property  # type: ignore[no-redef]
    def valign(self) -> Optional[str]:
        """getter of valign"""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[Literal["bottom", "center", "top"]]) -> None:
        """setter of valign"""
        if isinstance(value, property) or value is None:
            self._valign = None
            return

        AlignValidator.validate_valign(value)
        self._valign = value

    @property  # type: ignore[no-redef]
    def color(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of color"""
        return self._color

    @color.setter
    def color(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of color"""
        if isinstance(value, property) or value is None:
            self._color = None
            return

        ColorValidator.validate_color(value)
        self._color = value

    @property  # type: ignore[no-redef]
    def alpha(self) -> Optional[float]:
        """getter of alpha"""
        return self._alpha

    @alpha.setter
    def alpha(self, value: Optional[float]) -> None:
        """setter of alpha"""
        if isinstance(value, property) or value is None:
            self._alpha = None
            return

        ColorValidator.validate_alpha(value)
        self._alpha = value

    @property  # type: ignore[no-redef]
    def size(self) -> Optional[float]:
        """getter of size"""
        return self._size

    @size.setter
    def size(self, value: Optional[float]) -> None:
        """setter of size"""
        if isinstance(value, property) or value is None:
            self._size = None
            return

        TextValidator.validate_size(value)
        self._size = value

    @property  # type: ignore[no-redef]
    def font(self) -> Union[
        Font,
        FontArabic,
        FontBase,
        FontSerif,
        FontSanSerif,
        FontChinese,
        FontJapanese,
        FontKorean,
        FontMonoSpace,
        FontRoboto,
        FontSourceCode,
        FontFile,
        None,
    ]:
        """getter of font"""
        return self._font

    @font.setter
    def font(
        self,
        value: Union[
            Font,
            FontArabic,
            FontBase,
            FontSerif,
            FontSanSerif,
            FontChinese,
            FontJapanese,
            FontKorean,
            FontMonoSpace,
            FontRoboto,
            FontSourceCode,
            FontFile,
            None,
        ],
    ) -> None:
        """setter of font"""
        if isinstance(value, property) or value is None:
            self._font = None
            return

        TextValidator.validate_font(value)
        self._font = value

    @property  # type: ignore[no-redef]
    def angle(self) -> Optional[float]:
        """getter of angle"""
        return self._angle

    @angle.setter
    def angle(self, value: Optional[float]) -> None:
        """setter of alpha"""
        if isinstance(value, property) or value is None:
            self._angle = None
            return

        CoordinateValidator.validate_angle(value)
        self._angle = value

    @property  # type: ignore[no-redef]
    def flip(self) -> Optional[bool]:
        """getter of flip"""
        return self._flip

    @flip.setter
    def flip(self, value: Optional[bool]) -> None:
        """setter of flip"""
        if isinstance(value, property) or value is None:
            self._flip = None
            return

        TextValidator.validate_flip(value)
        self._flip = value

    @property  # type: ignore[no-redef]
    def xy_shift(self) -> Optional[Tuple[float, float]]:
        """getter of xy_shift"""
        return self._xy_shift

    @xy_shift.setter
    def xy_shift(self, value: Optional[float]) -> None:
        """setter of xy_shift"""
        if isinstance(value, property) or value is None:
            self._xy_shift = None
            return

        CoordinateValidator.validate_xy(value)
        self._xy_shift = value


class TextStyleDefault:
    alpha: Final[float] = None
    color: Final[Tuple[int, int, int]] = Colors.Black
    size: Final[float] = 16
    halign: Final[str] = "center"
    valign: Final[str] = "center"
    font: Final[Font] = Font.SANSSERIF_REGULAR
    bgalpha: Final[None] = None
    bgfcolor: Final[None] = None
    # they will be applied if one of them is not None
    bglcolor: Final[Tuple[int, int, int]] = Colors.Black
    bglstyle: Final[str] = "solid"
    bglwidth: Final[float] = 1.0


@dataclasses.dataclass
class TextStyle:
    """drawlib text style dataclass.

    Instead of providing lots of style parameters to drawing text
    functions ``text()`` etc,
    user set text style to text this way.

    1. Provide text style settings to ``TextStyle``.
    2. Provide the style instance to functions which uses text style.
    3. Text style is applied to drawn text.

    It is easy for managing text styles and applying them to lots of texts.

    """

    alpha: Optional[float] = None
    color: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
    size: Union[float, str, None] = None
    halign: Optional[Literal["left", "center", "right"]] = None
    valign: Optional[Literal["bottom", "center", "top"]] = None
    font: Union[
        Font,
        FontArabic,
        FontBase,
        FontSerif,
        FontSanSerif,
        FontChinese,
        FontJapanese,
        FontKorean,
        FontMonoSpace,
        FontRoboto,
        FontSourceCode,
        FontFile,
        None,
    ] = None

    # background
    bgalpha: Optional[float] = None
    bglcolor: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
    bglstyle: Optional[Literal["solid", "dashed", "dotted", "dashdot"]] = None
    bglwidth: Optional[float] = None
    bgfcolor: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None

    @property  # type: ignore[no-redef]
    def halign(self) -> Optional[str]:
        """getter of halign"""
        return self._halign

    @halign.setter
    def halign(self, value: Optional[Literal["left", "center", "right"]]) -> None:
        """setter of halign"""
        if isinstance(value, property) or value is None:
            self._halign = None
            return

        AlignValidator.validate_halign(value)
        self._halign = value

    @property  # type: ignore[no-redef]
    def valign(self) -> Optional[str]:
        """getter of valign"""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[Literal["bottom", "center", "top"]]) -> None:
        """setter of valign"""
        if isinstance(value, property) or value is None:
            self._valign = None
            return

        AlignValidator.validate_valign(value)
        self._valign = value

    @property  # type: ignore[no-redef]
    def color(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of color"""
        return self._color

    @color.setter
    def color(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of color"""
        if isinstance(value, property) or value is None:
            self._color = None
            return

        ColorValidator.validate_color(value)
        self._color = value

    @property  # type: ignore[no-redef]
    def alpha(self) -> Optional[float]:
        """getter of alpha"""
        return self._alpha

    @alpha.setter
    def alpha(self, value: Optional[float]) -> None:
        """setter of alpha"""
        if isinstance(value, property) or value is None:
            self._alpha = None
            return

        ColorValidator.validate_alpha(value)
        self._alpha = value

    @property  # type: ignore[no-redef]
    def size(self) -> Optional[float]:
        """getter of size"""
        return self._size

    @size.setter
    def size(self, value: Optional[float]) -> None:
        """setter of size"""
        if isinstance(value, property) or value is None:
            self._size = None
            return

        TextValidator.validate_size(value)
        self._size = value

    @property  # type: ignore[no-redef]
    def font(self) -> Union[
        Font,
        FontArabic,
        FontBase,
        FontSerif,
        FontSanSerif,
        FontChinese,
        FontJapanese,
        FontKorean,
        FontMonoSpace,
        FontRoboto,
        FontSourceCode,
        FontFile,
        None,
    ]:
        """getter of font"""
        return self._font

    @font.setter
    def font(
        self,
        value: Union[
            Font,
            FontArabic,
            FontBase,
            FontSerif,
            FontSanSerif,
            FontChinese,
            FontJapanese,
            FontKorean,
            FontMonoSpace,
            FontRoboto,
            FontSourceCode,
            FontFile,
            None,
        ],
    ) -> None:
        """setter of font"""
        if isinstance(value, property) or value is None:
            self._font = None
            return

        TextValidator.validate_font(value)
        self._font = value

    @property  # type: ignore[no-redef]
    def bgalpha(self) -> Optional[float]:
        """getter of bgalpha"""
        return self._bgalpha

    @bgalpha.setter
    def bgalpha(self, value: Optional[float]) -> None:
        """setter of bgalpha"""
        if isinstance(value, property) or value is None:
            self._bgalpha = None
            return

        ColorValidator.validate_alpha(value)
        self._bgalpha = value

    @property  # type: ignore[no-redef]
    def bglwidth(self) -> Optional[float]:
        """getter of bglwidth"""
        return self._bglwidth

    @bglwidth.setter
    def bglwidth(self, value: Optional[float]) -> None:
        """setter of bglwidth"""
        if isinstance(value, property) or value is None:
            self._bglwidth = None
            return

        LineValidator.validate_width(value)
        self._bglwidth = value

    @property  # type: ignore[no-redef]
    def bglstyle(self) -> Optional[str]:
        """getter of bglstyle"""
        return self._bglstyle

    @bglstyle.setter
    def bglstyle(self, value: Optional[str]) -> None:
        """setter of bglstyle"""
        if isinstance(value, property) or value is None:
            self._bglstyle = None
            return

        LineValidator.validate_style(value)
        self._bglstyle = value

    @property  # type: ignore[no-redef]
    def bglcolor(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of bglcolor"""
        return self._bglcolor

    @bglcolor.setter
    def bglcolor(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of bglcolor"""
        if isinstance(value, property) or value is None:
            self._bglcolor = None
            return

        ColorValidator.validate_color(value)
        self._bglcolor = value

    @property  # type: ignore[no-redef]
    def bgfcolor(self) -> Union[Tuple[int, int, int], Tuple[int, int, int, float], None]:
        """getter of bgfcolor"""
        return self._bgfcolor

    @bgfcolor.setter
    def bgfcolor(self, value: Union[Tuple[int, int, int], Tuple[int, int, int, float], None]) -> None:
        """setter of fcolor"""
        if isinstance(value, property) or value is None:
            self._bgfcolor = None
            return

        ColorValidator.validate_color(value)
        self._bgfcolor = value
