import reflex as rx
import link_bio.utils as utils
from link_bio.routes import Route
from link_bio.team.navbar_team import navbar
from components.footer import footer
from views.header.links.links import links
import styles.styles as styles
from styles.styles import Size
from link_bio.team.team_content import team_content
from link_bio.team.header_team import header_team


@rx.page(
        title=utils.spage_title,
        description=utils.spage_description
)
def second() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.vstack(
            header_team(),
            team_content(),
            rx.vstack(
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=Size.BIG.value,
                align_items="center",
                margin="auto"
        )),
        footer()
    )