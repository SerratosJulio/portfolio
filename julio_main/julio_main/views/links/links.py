import reflex as rx
from julio_main.components.link_button import link_button

def links() -> rx.Component:
    
    return rx.vstack(

        link_button("LinkedIn","https://linkedin.com"),
        link_button("GitHub", "https://lgithub.com"),
        link_button("Social Media","https://facebook.com")
    
    
    )