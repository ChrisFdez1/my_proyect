import reflex as rx
import styles.styles as styles
from styles.colors import Color
from styles.colors import TextColor
import link_bio.routes as Route

def navbar() -> rx.Component:
    return rx.center(
        rx.box(
            rx.text(
            "Gente rotísima",
            style=styles.navbar_title_style,
            as_="span",
            color=Color.PRIMARY.value
            )
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index="999",
        top="0"
    )
