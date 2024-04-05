import reflex as rx
from julio_main.components.link_icon import link_icon
from julio_main.components.info_text import info_text

from julio_main.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name = "Julio", size = "xl"),
            rx.vstack(
                rx.heading(
                    "Jules", 
                    size = "lg"),
                
                rx.text(
                        "@serratos_con_ese",
                        margin_top = "0px !important"
                        ),

                        rx.hstack(
                            link_icon("Instagram.com"),
                            link_icon("Facebook")
                        ),
                        align_items = "start"
                    
            ),
            spacing = Size.DEFAULT.value
        ),

        rx.flex(

            info_text("8","of experience"),
            rx.spacer(),
            info_text("8","Example 2"),
            rx.spacer(),
            info_text("8","Example 3"),
            
            width = "100%"



        ),

        rx.text("Data Engineer"),
        spacing = Size.BIG.value,
        align_items = "start"

    )
