import reflex as rx #import reflex library
from julio_main.components.navbar import navbar
from julio_main.views.header.header import header
from julio_main.views.links.links import links
from julio_main.components.footer import footer

class State(rx.State):
    pass 

def index () -> rx.Component: #index function
    
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()

    )


    

app = rx.App()
app.add_page(index)
app.compile



