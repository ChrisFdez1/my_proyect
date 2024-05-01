import reflex as rx
from components.link_icon import link_icon
import styles.styles as styles
from components.info_text import info_text
from styles.colors import Color
from styles.colors import TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.avatar(
                      size="6",
                      src="/logo.jpg",
                      color=TextColor.BODY.value,
                      bg=Color.CONTENT.value,
                      padding="2px",
                      border="4px",
                      border_color=Color.PRIMARY.value,
                      spacing="2"
                      ),
        rx.vstack(
            rx.heading("christian Fernández"),
            rx.text(
                "@ChrisFdez",
                margin_top="0px !important",
                color=TextColor.BODY.value,
                ),
            )
        ),
        rx.text(
            "Hola, si entraste aquí debes ser un autentico crack, no tengo mucho más que agregar de momento asi que un saludo y que pases bien. ",
            color=TextColor.BODY.value,
            align="center",
            margin="auto"
            ),
        align="center",
        spacing="2",
        margin="auto"
    )