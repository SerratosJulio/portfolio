import reflex as rx
import julio_main.styles.styles as styles


def link_button(title: str, body: str, url: str) -> rx.Component:

    return rx.link (
        rx.button (
            rx.hstack(
                rx.icon(
                    tag="arrow_forward",
                    width = styles.Size.DEFAULT.value,
                    height = styles.Size.DEFAULT.value
                ),
                rx.vstack(

                    rx.text(title, style = styles.button_title_style),
                    rx.text(title, style = styles.button_body_style),
                    align_items = "start"
                )                
            )

        ),

        href = "linkedin.com.mx",
        is_external = True,
        width = "100%",
        text_decoration = "none"



    )


