import reflex as rx
import styles.styles as styles
from pages.index import index
from pages.second_page import second


class State(rx.State):
    pass


app = rx.App(
    style=styles.BASE_STYLE
)