import reflex as rx
import datetime
from julio_main.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(

        rx.image(src = "favicon.ico"),
        rx.text(f"2023 { datetime.date.today().year} - Julio Serratos, Copy Rigth"),
        margin_botton = Size.BIG.value,
        margin_top = "0px !important"

    )