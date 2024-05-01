import reflex as rx
from enum import Enum
from .colors import Color as color
from .colors import TextColor as TextColor
from styles.fonts import Font
from styles.fonts import FontWeigth

# Constans
MAX_WIDTH = "1920px"


STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=comfortaa:wght@500&display=swap"
]




# Sizes
class Size(Enum):
    SMALL = "em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "5em"
    MEDIUM_LARGE ="1.2em"


# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeigth.LIGHT.value,
    "background_color": color.BACKGROUND.value,
    rx.heading: {
        "size": "6",
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeigth.MEDIUM.value
    },

    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": color.CONTENT.value,
        "white_space": "normal",
        "text_aling": "start",
        "_hover": {
            "background_color": color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeigth.MEDIUM.value,
    font_size=Size.LARGE.value
        )

title_style = dict(
        width="100%",
        padding_top= Size.DEFAULT.value,
        color=color.PRIMARY.value,

)


button_title_style = dict(
    font_size = Size.MEDIUM_LARGE.value,
    color=TextColor.HEADER.value,
    font_family=Font.TITLE.value,
    font_weight= FontWeigth.MEDIUM.value
)

button_body_style = dict(
    font_weight= FontWeigth.LIGHT.value,
    font_size = Size.DEFAULT.value,
    color=TextColor.BODY.value,
    )
