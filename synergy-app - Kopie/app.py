import streamlit as st
# PAGE CONFIG
st.set_page_config(
    page_title='Development Banks Collaboration Analyzer',
    page_icon='📋',
    layout='wide',
)

from modules.navbar import show_navbar
import similarity_page

# reduce space to the top
st.markdown("""
        <style>
            .block-container {
                    padding-top: 1rem;
                    padding-bottom: 4rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }
        </style>
        """, unsafe_allow_html=True)

# NAVBAR
navbar = show_navbar()
#similarity_page.show_multi_matching_page()

