import streamlit as st
import pandas as pd
import numpy as np

from importlib.machinery import SourceFileLoader
crs_overlap = SourceFileLoader("crs_overlap", "nlp/crs_overlap.py").load_module()

# Read in CRS CODELISTS
crs3_df = pd.read_csv('src/codelists/crs3_codes.csv')
CRS3_CODES = crs3_df['code'].tolist()
CRS3_NAME = crs3_df['name'].tolist()
CRS3_MERGED = {f"{name} - {code}": code for name, code in zip(CRS3_NAME, CRS3_CODES)}

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
            options = CRS3_MERGED,
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
        
    if crs3_option != None:
        crs3_str = str(CRS3_MERGED[crs3_option])
        country_name = str(country_option[0])
        country_code = country_df[country_df['Country'] == country_name]['Alpha-2 code'].values[0].replace('"', "").strip(" ")
        result_df = crs_overlap.calc_crs3(crs3_str, country_code)

        st.dataframe(data=result_df)
