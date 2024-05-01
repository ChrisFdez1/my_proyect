import reflex as rx
import styles.styles as styles
from styles.colors import Color
from styles.colors import TextColor
from styles.styles import Size

def link_button(title: str, body: str, url: str, image: str, link:bool=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width="9%",
                    height="auto",
                    color=Color.PRIMARY.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                    ),
                    rx.vstack(
                        rx.text(title, style=styles.button_title_style),
                        rx.text(body, style=styles.button_body_style),
                        align_items="start",
                        margin="0",
                        spacing="2",
                        padding_y=Size.SMALL.value,
                        padding_right=Size.SMALL.value,
                                ),
                                width="100%",
                ),
        
        ),
        href=url, 
        is_external=link,
        width="auto",
        height="100%",
        align="center",
        margin="auto"
    )