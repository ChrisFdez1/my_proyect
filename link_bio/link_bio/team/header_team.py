import reflex as rx
from components.link_icon import link_icon
import styles.styles as styles
from components.info_text import info_text
from styles.colors import Color
from styles.colors import TextColor
from link_bio.team.name_link import link

def header_team() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.avatar(
                    size="8",
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
            link("@ChrisFdez", "https://www.youtube.com/channel/UC0xXSNPB2Xi9yJf8XbnfdtQ")
            )
        ),
        rx.text(
            "Vida antes que muerte. Fuerza antes que debilidad. Viaje antes que destino ",
            color=TextColor.BODY.value,
            align="center",
            margin="auto"
            ),
        align="center",
        spacing="2",
        margin="auto"
    )