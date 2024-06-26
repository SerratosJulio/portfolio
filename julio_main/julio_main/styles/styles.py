from enum import Enum
import reflex as rx

#constants
MAX_WIDTH = "600px"


# sizes

class Size(Enum):
    SMALL = "0.5em" 
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"


#styles
    

BASE_STYLE = {
    rx.button: {
        "width"  : "100%",
        "height" : "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius":  Size.DEFAULT.value
        },

    rx.link: {
        "text_decoration" : "none",
        "_hover" : {}

        }
}



title_style = dict (

    size = "lg",
    width = "100%",
    padding_top =  Size.DEFAULT.value
)

button_title_style = dict (
    font_size = Size.DEFAULT.value
)


button_body_style = dict (
    font_size = Size.MEDIUM.value
)


