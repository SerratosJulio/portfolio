import reflex as rx
from julio_main.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(

            "Julio Serratos",
            height = "40px"    
        ), 
        position = 'sticky',
        bg = "ligthgray",
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        z_index = "999",
        top = "0"

    )