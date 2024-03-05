import streamlit as st
import pandas as pd
#from nlp.crs_overlap import calc_crs3

# Read in CRS CODELISTS
crs3_df = pd.read_csv('src/codelists/crs3_codes.csv')
CRS3_CODES = crs3_df['code'].tolist()
CRS3_NAME = crs3_df['name'].tolist()
CRS3_SLECTION = {f"{name} - {code}": code for name, code in zip(CRS3_NAME, CRS3_CODES)}

# Read in countries from codelist
country_df = pd.read_csv('src/codelists/country_codes_ISO3166-1alpha-2.csv')
COUNTRY_CODES = country_df['Alpha-2 code'].tolist()
CRS3_NAMES = country_df['Country'].tolist()

def show_page():
    col1, col2 = st.columns([1, 1])
    with col1:
        crs3_option = st.selectbox(
            label = 'CRS3 Code',
            index = None,
            placeholder = " ",
            options = CRS3_SLECTION,
            )
        
        crs5_option = st.selectbox(
            label = 'CRS5 Code',
            index = None,
            placeholder = " ",
            options = ('Email', 'Home phone', 'Mobile phone'),
            disabled=True
            )

    with col2:
        country_option = st.multiselect(
            'Country / Countries',
            CRS3_NAMES
            )
