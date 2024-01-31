import reflex as rx
import julio_main.styles.styles as styles


def link_button(title: str, body: str, url: str) -> rx.Component:

    return rx.link (
        rx.button (
            rx.hstack(
                rx.icon(
                    tag="arrow_forward"
                ),
                rx.vstack(

                    rx.text(title, style = styles.button_title_style),
                    rx.text(title, style = styles.button_body_style)
                )                
            )

        ),

        href = "linkedin.com",
        is_external = True,
        width = "100%",
        text_decoration = "none"



    )


