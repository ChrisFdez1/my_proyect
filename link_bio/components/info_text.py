import reflex as rx
import styles.styles as styles
from styles.colors import TextColor
from styles.colors import Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, 
                font_weight="bold", 
                color=Color.PRIMARY.value, 
                as_="span"),
        f"{body}", font_size=styles.Size.SMALL.value,
        color=TextColor.BODY.value
    )