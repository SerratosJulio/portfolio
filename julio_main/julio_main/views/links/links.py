import reflex as rx
from julio_main.components.link_button import link_button
from julio_main.components.title import title


def links() -> rx.Component:
    
    return rx.vstack(

        title("Julio Serratos"),

        link_button("LinkedIn",
                    "Professional experience", 
                    "https://linkedin.com"
                      ),
        
        link_button("GitHub", 
                    "Portfolio of projects",
                    "https://lgithub.com"
                    ),


        link_button("Social Media",
                    "Follow my day and day",
                    "https://facebook.com"
                    ),
        
        width = "100%"
    
    
    )