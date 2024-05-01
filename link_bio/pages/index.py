import reflex as rx
import link_bio.utils as utils
from components.navbar import navbar
from components.footer import footer
from views.header.header import header
from views.header.links.links import links
import styles.styles as styles
from styles.styles import Size



@rx.page(
        title=utils.index_title,
        description=utils.index_description
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.vstack(
            header(),
            rx.vstack(
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=Size.BIG.value,
                align_items="center",
                margin="auto"
        )),
        footer()
    )