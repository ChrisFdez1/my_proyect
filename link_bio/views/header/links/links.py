import reflex as rx
from components.link_button import link_button
from components.title import title
from views.header.links import constans as const
from styles.colors import TextColor
from styles.styles import title_style
from styles.styles import color
import link_bio.routes as Route

def links() -> rx.Component:
        return rx.vstack(        
        title("Sobre mi"),
        rx.text("Para lo que llevo de vida realmente no tengo nada impresionante que aportar, es como si fuera un npc más en el mundo, pero por mis cojones que seré más que eso. Por ahora he pasado mi vida jugando videjuegos, estudiando y actualmente dedicandole tiempo a aprender python para poder crear aplicaciones o páginas web. Es el principio de algo maravilloso y espero conseguir todas mis metas en el futuro.",
                color=TextColor.BODY.value,
                align="center",
                margin="auto"),
        
        title("joyas de los videjuegos"),
        rx.text("como no se que poner en esta página por aquí abajo agregare algunas de las joyitas que me han entretenido por horas y que son de esas cosas que me gustaría olvidar para pasarmelo desde cero de nuevo.",
                color=TextColor.BODY.value,
                align="center",
                margin="auto"),
        rx.text("Hollow Knight", color=color.CONTENT.value,
                size="5",
                align="center",
                margin="auto"),
        rx.image(
        src="/hollow.webp",
        align="center",
        margin="auto",
        ),
        rx.text("Al principio cuando instalé el juego no me llamaba mucho la atención, de hecho llegué a desinstalarlo, luego le di una oportunidad y es de las mejores desiciones que he tomado.",
                color=TextColor.BODY.value,
                align="center",
                margin="auto"),
        
        title("2"),
        rx.text("The binding of isaac", color=color.CONTENT.value,
        size="5",
        align="center",
        margin="auto"),

        rx.image(
        src="/isaac.webp",
        align="center",
        margin="auto"
        ),
        rx.text("mas de mil horas de vicio en este juego, cada run distinta, y momentos de risa y frustación con ciertos personajes",
                color=TextColor.BODY.value,
                align="center",
                margin="auto"),
        
        title("Mis redes para que me sigas... Si quieres"),
        link_button("twich", "existe por alguna razón y eso", const.TWICH_URL, "/icons/twitch.svg"),
        link_button("Youtube", "tambien cuenta de youtube", const.YOUTUBE_URL, "/icons/youtube.svg"),
        link_button("twitter", "twitter sigue siendo twitter", const.YOUTUBE_URL, "/icons/twitter.svg"),
        
        title("email por si quieres patrocinarme"),
        link_button("Email", const.EMAIL_URL, f"mailto:{const.EMAIL_URL}", "/icons/envelope-solid.svg"),

        width="100%",
        spacing="2"
)
