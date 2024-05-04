# Copyright (c) 2024 Yuichi Ito (yuichi@yuichi.com)
#
# This software is licensed under the Apache License, Version 2.0.
# For more information, please visit: https://github.com/yuichi110/drawlib
#
# This software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.

"""Drawlib style theme

Define style theme at class ``Theme``.
Default or choosed theme is applied if style is not provided.
Instance ``dtheme``  is provided to user to control theme.

"""

import dataclasses
from typing import Optional, Dict, Tuple, Union, Literal, List
from copy import deepcopy

from drawlib.v0_1.private.util import error_handler
from drawlib.v0_1.private.core.model import (
    IconStyle,
    ImageStyle,
    LineStyle,
    LineArrowStyle,
    ShapeStyle,
    ShapeTextStyle,
    TextStyle,
)
from drawlib.v0_1.private.core.fonts import (
    FontBase,
    Font,
    FontSourceCode,
)
from drawlib.v0_1.private.arg_validator import ArgValidator


@dataclasses.dataclass
class _ThemeStyle:
    """Helper dataclass for defining theme styles"""

    # icon
    icon_style: Literal["thin", "light", "regular", "bold", "fill"]
    icon_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]

    # line
    line_style: Literal["solid", "dashed", "dotted", "dashdot"]
    line_width: float
    line_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]
    arrowhead_style: Literal[
        "->",
        "<-",
        "<->",
        "-|>",
        "<|-",
        "<|-|>",
    ]
    arrowhead_scale: int

    # shape
    shape_line_style: Literal["solid", "dashed", "dotted", "dashdot"]
    shape_line_width: float
    shape_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
        None,
    ]
    shape_line_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
        None,
    ]
    shape_fill_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
        None,
    ]

    # shapetext
    shapetext_font: FontBase
    shapetext_size: int
    shapetext_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]

    # text
    text_font: FontBase
    text_size: int
    text_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]


class Theme:
    """Drawlib Thema control class.

    * define theme here
    * provide theme access methods

    """

    @error_handler
    def __init__(self):
        self.theme_default()

    #############
    ### Thema ###
    #############

    @error_handler
    def theme_initialize(self) -> None:
        """Initialize theme.

        This method need to be called before setting manual theme.

        Returns:
            None

        """

        self._background: Tuple[float, float, float, float] = (255, 255, 255, 1)
        self._sourcecode_font: FontSourceCode = FontSourceCode.SOURCECODEPRO

        # icon
        self._iconstyles: Dict[str, IconStyle] = {}

        # image
        self._imagestyles: Dict[str, ImageStyle] = {}

        # line
        self._linestyles: Dict[str, LineStyle] = {}
        self._linearrowstyles: Dict[str, LineArrowStyle] = {}

        # shape
        self._shapestyles: Dict[str, ShapeStyle] = {}
        self._shapestyles_arc: Dict[str, ShapeStyle] = {}
        self._shapestyles_arrow: Dict[str, ShapeStyle] = {}
        self._shapestyles_circle: Dict[str, ShapeStyle] = {}
        self._shapestyles_ellipse: Dict[str, ShapeStyle] = {}
        self._shapestyles_polygon: Dict[str, ShapeStyle] = {}
        self._shapestyles_rectangle: Dict[str, ShapeStyle] = {}
        self._shapestyles_regularpolygon: Dict[str, ShapeStyle] = {}
        self._shapestyles_wedge: Dict[str, ShapeStyle] = {}
        self._shapetextstyles: Dict[str, ShapeTextStyle] = {}

        # text
        self._textstyles: Dict[str, TextStyle] = {}

    @error_handler
    def theme_default(self) -> None:
        """Change theme to default.

        Returns:
            None

        """

        # https://coolors.co/6d7cc5-70c2bf-e4dfda-d4b483-c1666b

        # primary color
        blue_light = _get_rgba_from_hex("#6D7CC5")
        blue_dark = _get_rgba_from_hex("#12152B")

        # secondary color
        green_light = _get_rgba_from_hex("#70C2BF")
        green_dark = _get_rgba_from_hex("#0C1D1C")

        # third color
        pink_light = _get_rgba_from_hex("#C1666B")
        pink_dark = _get_rgba_from_hex("#1D0C0D")

        tstyle1 = _ThemeStyle(
            icon_style="thin",
            icon_color=blue_dark,
            line_style="solid",
            line_width=2,
            line_color=blue_dark,
            arrowhead_style="->",
            arrowhead_scale=20,
            shape_line_style="solid",
            shape_line_width=1,
            shape_line_color=blue_dark,
            shape_fill_color=blue_light,
            shape_color=None,
            shapetext_font=Font.SANSSERIF_REGULAR,
            shapetext_size=16,
            shapetext_color=blue_dark,
            text_font=Font.SANSSERIF_REGULAR,
            text_size=16,
            text_color=blue_dark,
        )

        tstyle2 = deepcopy(tstyle1)
        tstyle2.line_color = green_dark
        tstyle2.shape_line_color = green_dark
        tstyle2.shape_fill_color = green_light
        tstyle2.shapetext_color = green_dark
        tstyle2.text_color = green_dark

        tstyle3 = deepcopy(tstyle1)
        tstyle3.line_color = pink_dark
        tstyle3.shape_line_color = pink_dark
        tstyle3.shape_fill_color = pink_light
        tstyle3.shapetext_color = pink_dark
        tstyle3.text_color = pink_dark

        self._apply_thema_styles(
            background=(255, 255, 255, 1),  # white
            sourcecode_font=FontSourceCode.SOURCECODEPRO,
            tstyle1=tstyle1,
            tstyle2=tstyle2,
            tstyle3=tstyle3,
        )

    @error_handler
    def theme_gray(self) -> None:
        """Change theme to gray.

        Returns:
            None

        """

        # https://coolors.co/palette/f8f9fa-e9ecef-dee2e6-ced4da-adb5bd-6c757d-495057-343a40-212529

        # primary color
        gray1 = _get_rgba_from_hex("#ADB5BD")
        gray_dark = _get_rgba_from_hex("#212529")

        # secondary color
        gray2 = _get_rgba_from_hex("#CED4DA")

        # third color
        gray3 = _get_rgba_from_hex("#DEE2E6")

        tstyle1 = _ThemeStyle(
            icon_style="thin",
            icon_color=gray_dark,
            line_style="solid",
            line_width=2,
            line_color=gray_dark,
            arrowhead_style="->",
            arrowhead_scale=20,
            shape_line_style="solid",
            shape_line_width=1,
            shape_line_color=gray_dark,
            shape_fill_color=gray1,
            shape_color=None,
            shapetext_font=Font.SANSSERIF_REGULAR,
            shapetext_size=16,
            shapetext_color=gray_dark,
            text_font=Font.SANSSERIF_REGULAR,
            text_size=16,
            text_color=gray_dark,
        )

        tstyle2 = deepcopy(tstyle1)
        tstyle2.shape_fill_color = gray2

        tstyle3 = deepcopy(tstyle1)
        tstyle3.shape_fill_color = gray3

        self._apply_thema_styles(
            background=(255, 255, 255, 1),  # white
            sourcecode_font=FontSourceCode.SOURCECODEPRO,
            tstyle1=tstyle1,
            tstyle2=tstyle2,
            tstyle3=tstyle3,
        )

    ##################
    ### Background ###
    ##################

    @error_handler
    def background_color_get(self) -> Tuple[int, int, int]:
        """Get theme background color.

        Returns:
            color

        """

        # has no alpha
        if len(self._background) == 3:
            return self._background

        # has alpha
        b = self._background
        return (b[0], b[1], b[2])

    @error_handler
    def background_color_set(
        self,
        color: Union[
            Tuple[int, int, int],
            Tuple[int, int, int, float],
        ],
    ) -> None:
        """Set theme background color.

        Args:
            color: background color. (R, G, B)

        Returns:
            None

        """

        ArgValidator.validate_color("color", color)
        self._background = color

    @error_handler
    def background_alpha_get(self) -> float:
        """Get theme background alpha.

        Returns:
            float: 0 ~ 1.0

        """

        # has no alpha
        if len(self._background) == 3:
            return 1.0

        # has alpha
        return self._background[3]

    @error_handler
    def background_alpha_set(self, alpha: float) -> None:
        """Set theme background alpha.

        Args:
            alpha: float. 0.0 ~ 1.0

        Returns:
            None

        """

        ArgValidator.validate_alpha("alpha", alpha)

        if len(self._background) == 3:
            # tuple + tuple makes concat tuple
            self._background = self._background + (alpha,)
            return

        self._background = self._background[:-1] + (alpha,)

    ############
    ### Icon ###
    ############

    @error_handler
    def iconstyle_get(self, name: str = "1") -> IconStyle:
        """Get theme IconStyle.

        Args:
            name(option): key

        Returns:
            IconStyle

        """

        return deepcopy(self._iconstyles[name])

    @error_handler
    def iconstyle_set(self, style: IconStyle, name: str = "1") -> None:
        """Set theme IconStyle.

        Args:
            style: theme IconStyle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_iconstyle("style", style)
        ArgValidator.validate_str("name", name)
        self._iconstyles[name] = deepcopy(style)

    ############
    ### Image ###
    ############

    @error_handler
    def imagestyle_get(self, name: str = "1") -> ImageStyle:
        """Get theme ImageStyle.

        Args:
            name(option): key

        Returns:
            ImageStyle

        """

        return deepcopy(self._imagestyles[name])

    @error_handler
    def imagestyle_set(self, style: ImageStyle, name: str = "1") -> None:
        """Set theme ImageStyle.

        Args:
            style: theme ImageStyle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_imagestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._imagestyles[name] = deepcopy(style)

    ############
    ### Line ###
    ############

    @error_handler
    def linestyle_get(self, name: str = "1") -> LineStyle:
        """Get theme LineStyle.

        Args:
            name(option): key

        Returns:
            LineStyle

        """

        return deepcopy(self._linestyles[name])

    @error_handler
    def linestyle_set(self, style: LineStyle, name: str = "1") -> None:
        """Set theme LineStyle.

        Args:
            style: theme LineStyle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_linestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._linestyles[name] = deepcopy(style)

    @error_handler
    def linearrowstyle_get(self, name: str = "1") -> LineArrowStyle:
        """Get theme LineArrowStyle.

        Args:
            name(optional): key

        Returns:
            LineArrowStyle

        """

        return deepcopy(self._linearrowstyles[name])

    @error_handler
    def linearrowstyle_set(self, style: LineArrowStyle, name: str = "1") -> None:
        """Set theme LineArrowStyle.

        Args:
            style: theme LineArrowStyle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_linearrowstyle("style", style)
        ArgValidator.validate_str("name", name)
        self._linearrowstyles[name] = deepcopy(style)

    ############
    ### Text ###
    ############

    @error_handler
    def textstyle_get(self, name: str = "1") -> TextStyle:
        """Get theme TextStyle.

        Args:
            name(optional): key

        Returns:
            TextStyle

        """

        return deepcopy(self._textstyles[name])

    @error_handler
    def textstyle_set(self, style: TextStyle, name: str = "1") -> None:
        """Set theme TextStyle.

        Args:
            style: theme TextStyle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_textstyle("style", style)
        ArgValidator.validate_str("name", name)
        self._textstyles[name] = deepcopy(style)

    @error_handler
    def sourcecodefont_get(self) -> FontSourceCode:
        """Get theme FontSourceCode.

        Returns:
            FontSourceCode

        """
        return self._sourcecode_font

    @error_handler
    def sourcecodefont_set(self, font: FontSourceCode) -> None:
        """Set theme FontSourceCode.

        Args:
            font: FontSourceCode

        Returns:
            None

        """
        ArgValidator.validate_fontsourcecode(font)
        self._sourcecode_font = font

    #############
    ### Shape ###
    #############

    @error_handler
    def shapestyle_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle.

        Args:
            style: theme ShapeStyle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles[name] = deepcopy(style)

    @error_handler
    def shapetextstyle_get(self, name: str = "1") -> ShapeTextStyle:
        """Get theme ShapeTextStyle.

        Args:
            name(optional): key

        Returns:
            ShapeTextStyle

        """

        return deepcopy(self._shapetextstyles[name])

    @error_handler
    def shapetextstyle_set(self, style: ShapeTextStyle, name: str = "1") -> None:
        """Set theme ShapeTextStyle.

        Args:
            style: theme ShapeTextStyle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapetextstyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapetextstyles[name] = deepcopy(style)

    @error_handler
    def shapestyle_arc_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for arc.

        If ShapeStyle is not set for arc, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_arc:
            return deepcopy(self._shapestyles_arc[name])
        style = deepcopy(self._shapestyles[name])
        style.fcolor = None  # arc default style doesn't have fill color
        return style

    @error_handler
    def shapestyle_arc_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for arc.

        Args:
            style: theme ShapeStyle for arc
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_arc[name] = deepcopy(style)

    @error_handler
    def shapestyle_arrow_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for arrow.

        If ShapeStyle is not set for arrow, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_arrow:
            return deepcopy(self._shapestyles_arrow[name])
        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_arrow_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for arrow.

        Args:
            style: theme ShapeStyle for arrow
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_arrow[name] = deepcopy(style)

    @error_handler
    def shapestyle_circle_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for circle.

        If ShapeStyle is not set for circle, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_circle:
            return deepcopy(self._shapestyles_circle[name])
        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_circle_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for circle.

        Args:
            style: theme ShapeStyle for circle
            name(optional): key

        Returns:
            None

        """
        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_circle[name] = deepcopy(style)

    @error_handler
    def shapestyle_ellipse_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for ellipse.

        If ShapeStyle is not set for ellipse, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_ellipse:
            return deepcopy(self._shapestyles_ellipse[name])
        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_ellipse_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for ellipse.

        Args:
            style: theme ShapeStyle for ellipse
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_ellipse[name] = deepcopy(style)

    @error_handler
    def shapestyle_polygon_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for polygon.

        If ShapeStyle is not set for polygon, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_polygon:
            return deepcopy(self._shapestyles_polygon[name])
        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_polygon_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for polygon.

        Args:
            style: theme ShapeStyle for polygon
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_polygon[name] = deepcopy(style)

    @error_handler
    def shapestyle_rectangle_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for rectangle.

        If ShapeStyle is not set for rectangle, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_rectangle:
            return deepcopy(self._shapestyles_rectangle[name])
        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_rectangle_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for rectangle.

        Args:
            style: theme ShapeStyle for rectangle
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_rectangle[name] = deepcopy(style)

    @error_handler
    def shapestyle_regularpolygon_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for regularpolygon.

        If ShapeStyle is not set for regularpolygon, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_regularpolygon:
            return deepcopy(self._shapestyles_regularpolygon[name])
        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_regularpolygon_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for regularpolygon.

        Args:
            style: theme ShapeStyle for regularpolygon
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_regularpolygon[name] = deepcopy(style)

    @error_handler
    def shapestyle_wedge_get(self, name: str = "1") -> ShapeStyle:
        """Get theme ShapeStyle for wedge.

        If ShapeStyle is not set for wedge, get general ShapeStyle.

        Args:
            name(optional): key

        Returns:
            ShapeStyle

        """

        if name in self._shapestyles_wedge:
            return deepcopy(self._shapestyles_wedge[name])
        return deepcopy(self._shapestyles[name])

    @error_handler
    def shapestyle_wedge_set(self, style: ShapeStyle, name: str = "1") -> None:
        """Set theme ShapeStyle for wedge.

        Args:
            style: theme ShapeStyle for wedge
            name(optional): key

        Returns:
            None

        """

        ArgValidator.validate_shapestyle("style", style)
        ArgValidator.validate_str("name", name)
        self._shapestyles_wedge[name] = deepcopy(style)

    ###############
    ### Private ###
    ###############

    def _apply_thema_styles(
        self,
        background: Union[Tuple[int, int, int], Tuple[int, int, int, float]],
        sourcecode_font: FontSourceCode,
        tstyle1: _ThemeStyle,
        tstyle2: Optional[_ThemeStyle] = None,
        tstyle3: Optional[_ThemeStyle] = None,
        tstyle4: Optional[_ThemeStyle] = None,
        tstyle5: Optional[_ThemeStyle] = None,
    ) -> None:

        self.theme_initialize()
        self._background = background
        self._sourcecode_font = sourcecode_font

        tstyles: List[_ThemeStyle] = [
            tstyle1,
            tstyle2,
            tstyle3,
            tstyle4,
            tstyle5,
        ]
        for i, tstyle in enumerate(tstyles, start=1):
            name = str(i)
            if tstyle is None:
                if name == "1":
                    raise ValueError('default thema style "1" must be configured.')
                continue

            self.iconstyle_set(
                style=IconStyle(
                    style=tstyle.icon_style,
                    color=tstyle.icon_color,
                ),
                name=name,
            )
            self.imagestyle_set(
                style=ImageStyle(
                    lstyle=tstyle.shape_line_style,
                    lcolor=tstyle.shape_line_color,
                ),
                name=name,
            )
            self.linestyle_set(
                style=LineStyle(
                    style=tstyle.line_style,
                    width=tstyle.line_width,
                    color=tstyle.line_color,
                ),
                name=name,
            )

            self.linearrowstyle_set(
                style=LineArrowStyle(
                    lstyle=tstyle.line_style,
                    lwidth=tstyle.line_width,
                    hstyle=tstyle.arrowhead_style,
                    hscale=tstyle.arrowhead_scale,
                    color=tstyle.line_color,
                ),
                name=name,
            )

            self.textstyle_set(
                style=TextStyle(
                    font=tstyle.text_font,
                    size=tstyle.text_size,
                    color=tstyle.text_color,
                    halign=None,  # depends on situation. keep None.
                    valign=None,  # depends on situation. keep None.
                ),
                name=name,
            )

            self.shapestyle_set(
                style=ShapeStyle(
                    lwidth=tstyle.shape_line_width,
                    lstyle=tstyle.shape_line_style,
                    lcolor=tstyle.shape_line_color,
                    fcolor=tstyle.shape_fill_color,
                    halign=None,  # depends on situation. keep None.
                    valign=None,  # depends on situation. keep None.
                ),
                name=name,
            )

            self.shapetextstyle_set(
                style=ShapeTextStyle(
                    font=tstyle.text_font,
                    size=tstyle.text_size,
                    color=tstyle.text_color,
                    halign=None,  # depends on situation. keep None.
                    valign=None,  # depends on situation. keep None.
                ),
                name=name,
            )


def _get_rgba_from_hex(hex_color: str) -> Tuple[int, int, int, float]:
    """
    Convert a hexadecimal color code to RGBA values.

    Args:
        hex_color (str): The hexadecimal color code (e.g., "#FF5733" or "#FFF").

    Returns:
        tuple[int, int, int, float]: A tuple containing the RGBA values (0-255 for R, G, B and 0.0-1.0 for A).
    """

    # Remove the '#' prefix if present
    hex_color = hex_color.lstrip("#")

    # Determine the length of the hex color code
    hex_length = len(hex_color)

    # Convert the hex code to RGB values
    if hex_length == 3:  # Short hex format (#RGB)
        r = int(hex_color[0] * 2, 16)
        g = int(hex_color[1] * 2, 16)
        b = int(hex_color[2] * 2, 16)
        a = 1.0
    elif hex_length in (6, 8):  # Full hex format (#RRGGBB)
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        if hex_length == 8:  # With alpha
            a = int(hex_color[6:8], 16)
        else:
            a = 1.0
    else:
        raise ValueError("Invalid hex color code format")

    return (r, g, b, a)


dtheme = Theme()
"""Singleton instance of class ``Theme``."""
