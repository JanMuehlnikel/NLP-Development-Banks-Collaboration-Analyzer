import streamlit as st
# PAGE CONFIG
st.set_page_config(
    page_title='Development Banks Collaboration Analyzer',
    page_icon='📋',
    layout='wide',
)

from utils.navbar import show_navbar
import home, sector, similarity

# NAVBAR
navbar = show_navbar()

# Navigation
if navbar == "Home":
    st.session_state.page = home.show_page()
elif navbar == "Sector Matches":
    pass
    #st.session_state.page = sector.show_page()
elif navbar == "Similarity Matches":
    st.session_state.page = similarity.show_page()

