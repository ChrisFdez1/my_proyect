import reflex as rx
import datetime
import styles.styles as styles
from styles.colors import Color
from styles.colors import TextColor
from views.header.links import constans
from styles.styles import Size

def footer() -> rx.Component:
    return rx.vstack(        
        rx.text(f"2024-{datetime.date.today().year} / No hay nada más que ver por aquí",
                font_size=styles.Size.MEDIUM.value,
                margin_top="0px important!"
                ),
        align="center",
        margin_botton=styles.Size.BIG.value,
        padding_botton="2",
        padding_x=styles.Size.BIG.value,
        color=TextColor.FOOTER.value
    )