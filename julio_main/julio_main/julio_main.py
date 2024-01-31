import reflex as rx #import reflex library
from julio_main.components.navbar import navbar
from julio_main.views.header.header import header
from julio_main.views.links.links import links
from julio_main.components.footer import footer
import julio_main.styles.styles as styles

class State(rx.State):
    pass 

def index () -> rx.Component: #index function
    
    return rx.box(
        
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width ="100%",
                margin_y = styles.Size.BIG.value
             ) #close vstack
        ),
        
        footer()
    )


    

app = rx.App(
    style = styles.BASE_STYLE)

app.add_page(index)
app.compile



