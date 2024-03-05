import streamlit as st
# PAGE CONFIG
st.set_page_config(
    page_title='Development Banks Collaboration Analyzer',
    page_icon='📋',
    layout='wide',
)

from utils.navbar import show_navbar
import home, crs

# NAVBAR
navbar = show_navbar()

# Navigation
if navbar == "Home":
    st.session_state.page = home.show_page()
elif navbar == "CRS":
    st.session_state.page = crs.show_page()

