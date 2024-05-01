import reflex as rx
from components.link_button import link_button
from link_bio.team.title_team import title
from views.header.links import constans as const
from styles.colors import TextColor
from styles.styles import title_style
from styles.styles import color
import link_bio.routes as Route
from styles.colors import Color
from styles.colors import TextColor
from link_bio.team.name_link import link


def team_content():
    return rx.vstack(
        title("El team"),
        rx.text(
            "Estos hijos de su putísima madre están siendo buscados por el FBI y la NASA.",
            color=TextColor.BODY.value,
            align="center",
            margin="auto",
            size="5"
        ),
        rx.vstack(
            rx.box(rx.avatar(
                    size="8",
                    src="/vera.jpg",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border="4px",
                    border_color=Color.PRIMARY.value,
                    spacing="2"
            ),
            rx.vstack(
                rx.heading("Ricardo Vera"),
                link("@Elias Vera", "https://www.facebook.com/profile.php?id=100033488892970"),
                rx.text("A este vato se lo conoce por haber contribuido con la fabricación de la bomba atomica que bombardeo hiroshima y le sabe a la espol.",    
                        color=TextColor.BODY.value,
                        align="center",
                        margin="auto")),
                        bg="#202021",
                        border_radius="10px",
                        margin="12px",
                        padding="12px"),
            
            rx.box(rx.avatar(
                size="8",
                src="/orellana.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
                spacing="2"
            ),
            rx.vstack(
            rx.heading("Jeremy Orellana"),
            link("@Jeremy Orellana", "https://www.facebook.com/jeremy.orellana.739"),
            rx.text("Cuidado con este wey nadie conoce su rostro y se dice que está secuestrando niños en las calles, este wey también le sabe a la espol.",    
                    color=TextColor.BODY.value,
                    align="center",
                    margin="auto")),
                    bg="#202021",
                    border_radius="10px",
                    margin="12px",
                    padding="12px"),

            rx.text("Recordad que nada nunca es eterno, de un momento a otro cualquier cosa podría acabar, los problemas también son una oprtunidad.",
                color=TextColor.BODY.value,
                align="center",
                margin="auto",
                size="5"
                ),

            rx.image(
            src="/str.png",
            align="center",
            margin="auto"
                    ),

            rx.text(
            "Leed el archivo de las tormentas 11/10 y god.",
                color=TextColor.BODY.value,
                align="center",
                margin="auto",
                size="5"
                )
            
        ),
        margin="auto"
    )