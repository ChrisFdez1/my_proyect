import reflex as rx

def link(text: str, url: str):
    return rx.link(
        text,
        href=url,
        is_external=True
    )