import pandas as pd
import streamlit as st

def country_option(special_cases, country_names):
    country_option = st.multiselect(
                'Country / Countries',
                special_cases + country_names,
                placeholder="Select"
                )
    
    return country_option

def orga_option(special_cases, orga_names):
    orga_list = special_cases + [f"{v[0]} ({k})" for k, v in orga_names.items()]
    orga_option = st.multiselect(
                'Development Bank / Organization',
                orga_list,
                placeholder="Select"
                )
    
    return orga_option