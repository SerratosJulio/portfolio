import reflex as rx

def header() -> rx.Component:
    return rx.vstack(

        rx.avatar(name = "Julio", size = "xl"),
        rx.text("Hello, welcome to Data Portfolio by Julio"),
        rx.text("Please explore...")

    )
