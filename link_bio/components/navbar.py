import reflex as rx
import styles.styles as styles
from styles.colors import Color
from styles.colors import TextColor
import link_bio.routes as Route
from components.ant_component import float_button


def navbar() -> rx.Component:
    return rx.center(
        rx.link(rx.box(
        rx.text(
            "Chris",
            style=styles.navbar_title_style,
            as_="span",
            color=Color.PRIMARY.value,
        ),
        ),
        href=Route.Route.Second_PAGE.value,
        ),
        rx.link(rx.box(
            rx.text(
            "_Fdez",
            style=styles.navbar_title_style,
            as_="span",
            color=Color.SECONDARY.value
            )
            ),
            href=Route.Route.Second_PAGE.value,
            ),
        float_button(),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index="999",
        top="0"
    )
