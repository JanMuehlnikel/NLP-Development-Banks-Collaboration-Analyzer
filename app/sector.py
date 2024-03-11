"""
Page to analyse the link between crs codes, countries and organizations
"""

################
# DEPENDENCIES #
################
import streamlit as st
import pandas as pd
import utils.crs_table as crs_table

from importlib.machinery import SourceFileLoader
crs_overlap = SourceFileLoader("crs_overlap", "data/models/crs_overlap.py").load_module()
CONSTANTS = SourceFileLoader("CONSTANTS", "config/CONSTANTS.py").load_module()

# CHACHE DATA
# FETCH NEEDED DATA AND STORE IN CHACHE MEMORY TO SAVE LOADING TIME
@st.cache_data
def getCRS3():
    # Read in CRS3 CODELISTS
    crs3_df = pd.read_csv('app/src/codelists/crs3_codes.csv')
    CRS3_CODES = crs3_df['code'].tolist()
    CRS3_NAME = crs3_df['name'].tolist()
    CRS3_MERGED = {f"{name} - {code}": code for name, code in zip(CRS3_NAME, CRS3_CODES)}

    return CRS3_MERGED

@st.cache_data
def getCRS5():
    # Read in CRS3 CODELISTS
    crs5_df = pd.read_csv('app/src/codelists/crs5_codes.csv')
    CRS5_CODES = crs5_df['code'].tolist()
    CRS5_NAME = crs5_df['name'].tolist()
    CRS5_MERGED = {code: [f"{name} - {code}"] for name, code in zip(CRS5_NAME, CRS5_CODES)}

    return CRS5_MERGED

@st.cache_data
def getSDG():
    # Read in SDG CODELISTS
    sdg_df = pd.read_csv('app/src/codelists/sdg_goals.csv')
    SDG_NAMES = sdg_df['name'].tolist()

    return SDG_NAMES

@st.cache_data
def getCountry():
    # Read in countries from codelist
    country_df = pd.read_csv('app/src/codelists/country_codes_ISO3166-1alpha-2.csv')
    COUNTRY_CODES = country_df['Alpha-2 code'].tolist()
    COUNTRY_NAMES = country_df['Country'].tolist()

    return country_df, COUNTRY_CODES, COUNTRY_NAMES

CRS3_MERGED = getCRS3()
CRS5_MERGED = getCRS5()
SDG_NAMES = getSDG()
country_df, COUNTRY_CODES, COUNTRY_NAMES = getCountry()

########
# PAGE #
########
def show_page():
    
    def show_crs():
        # SESSION STATES
        st.session_state.crs5_option_disabled = True

        # SELECTION
        col1, col2 = st.columns([1, 1])
        with col1:
            # CRS3 CODE SELECT
            crs3_option = st.selectbox(
                label = 'CRS3 Code',
                index = None,
                placeholder = "Select",
                options = CRS3_MERGED,
                )
            
            # CRS5 CODE SELECT
            # Only enable crs5 select field when crs3 code is selected
            if crs3_option:
                st.session_state.crs5_option_disabled = False

            # define list of crs5 codes dependend on crs3 codes
            crs5_list = [txt[0].replace('"', "") for code, txt in CRS5_MERGED.items() if str(code)[:3] == str(crs3_option)[-3:]]
            # crs5 select field
            crs5_option = st.selectbox(
                label = 'CRS5 Code',
                index = None,
                placeholder = "Select",
                options = crs5_list,
                disabled=st.session_state.crs5_option_disabled
                )

        with col2:
            # COUNTRY SELECTION
            country_option = st.multiselect(
                'Country / Countries',
                COUNTRY_NAMES,
                placeholder="Select"
                )
            
            # ORGA SELECTION
            orga_list = [f"{v[0]} - {k}" for k, v in CONSTANTS.ORGANIZATIONS.items()]
            orga_option = st.multiselect(
                'Development Bank / Organization',
                orga_list,
                placeholder="Select"
                )
        
        # SHOW RESULTS
        # Extract Orgas from multiselect
        selected_orgas = [str(o).split(" - ")[1] for o in orga_option]
        selected_orgas_code = [CONSTANTS.ORGANIZATIONS[o][2] for o in selected_orgas]
        # CRS table
        if crs3_option != None:
            if country_option != []:
                crs3_str = str(CRS3_MERGED[crs3_option])
                country_names = [str(c) for c in country_option]

                country_codes = [ 
                    country_df[country_df['Country'] == c]['Alpha-2 code'].values[0].replace('"', "").strip(" ")
                    for c in country_names
                    ]
                result_df = crs_overlap.calc_crs3(crs3_str, country_codes, selected_orgas_code)
                
                if crs5_option != None:
                    crs5_str = str(crs5_option[-5:])
                    result_df = crs_overlap.calc_crs5(crs5_str, country_codes, selected_orgas_code)
                
                # TABLE FOR CRS OVERLAP
                crs_table.show_table(result_df)

    def show_sdg():
        # SELECTION
        col1, col2 = st.columns([1, 1])
        with col1:
            # CRS3 CODE SELECT
            sdg_option = st.selectbox(
                label = 'SDG',
                index = None,
                placeholder = "Select SDG",
                options = SDG_NAMES,
                )

        with col2:
            # COUNTRY SELECTION
            country_option = st.multiselect(
                'Country / Countries',
                COUNTRY_NAMES,
                placeholder="Select"
                )
            
            # ORGA SELECTION
            orga_list = [f"{v[0]} - {k}" for k, v in CONSTANTS.ORGANIZATIONS.items()]
            orga_option = st.multiselect(
                'Development Bank / Organization',
                orga_list,
                placeholder="Select"
                )
            

        # SHOW RESULTS
        # Extract Orgas from multiselect
        selected_orgas = [str(o).split(" - ")[1] for o in orga_option]
        selected_orgas_code = [CONSTANTS.ORGANIZATIONS[o][2] for o in selected_orgas]
        # CRS table
        if sdg_option != None:
            if country_option != []:
                sdg_str = str(SDG_NAMES[sdg_option])
                country_names = [str(c) for c in country_option]

                country_codes = [ 
                    country_df[country_df['Country'] == c]['Alpha-2 code'].values[0].replace('"', "").strip(" ")
                    for c in country_names
                    ]
                result_df = sdg_overlap.calc_crs3(sdg_str, country_codes, selected_orgas_code)
                
                # TABLE FOR CRS OVERLAP
                sdg_table.show_table(result_df)

    # SELECT IF CRS or SDG Match
    match_option = st.selectbox(
                label = 'Matching Method',
                index = 0,
                placeholder = "Select",
                options = ["CRS", "SDG"],
                )         
    
    st.write("------------------")

    if match_option == "CRS":
        show_crs()
    elif match_option == "SDG":
        show_sdg()

