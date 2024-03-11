import streamlit as st
from streamlit_option_menu import option_menu # https://github.com/victoryhb/streamlit-option-menu

# giz-dsc colors
# orange: #e5b50d
# green: #48d47b
# blue: #0da2dc
# grey: #dadada

# giz colors https://www.giz.de/cdc/en/html/59638.html
# red: #c80f0f 
# grey: #6f6f6f
# light_grey: #b2b2b2
# light_red: #eba1a3

def show_navbar():
    navbar = option_menu(None, ["Home", "Sector Matches", 'Similarity Matches'], 
        icons=['house', 'list-task', "list-task", 'list-task'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#F0F0F0"  
            },
            "icon": {
                "color": "#c80f0f",  
                "font-size": "25px"
            },
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin":"0px",
                "--hover-color": "#b2b2b2"  
            },
            "nav-link-selected": {
                "background-color": "#F0F0F0"  
            },
            "nav-link-text": {
                "color": "#333333"  
            },

            "icon-active": {
                "color": "#dadada"  
            }
        }
    )

    return navbar