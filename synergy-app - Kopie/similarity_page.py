"""
Page for similarities
"""

################
# DEPENDENCIES #
################
import streamlit as st
import pandas as pd
from scipy.sparse import load_npz
import pickle
from sentence_transformers import SentenceTransformer
from modules.multimatch_result_table import show_multi_table
from modules.singlematch_result_table import show_single_table
from functions.filter_projects import filter_projects
from functions.filter_single import filter_single
from functions.calc_matches import calc_matches
from functions.same_country_filter import same_country_filter
from functions.single_similar import find_similar
#import psutil
import os
import gc

"""
def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024) 
"""

# Catch DATA

# Load Similarity matrix
"""
@st.cache_data
def load_sim_matrix():
    loaded_matrix = load_npz("src/extended_similarities.npz")
    dense_matrix = loaded_matrix.toarray().astype('float16')

    return dense_matrix
"""
@st.cache_data
def load_sim_matrix():
    loaded_matrix = load_npz("src/extended_similarities.npz")
    #dense_matrix = loaded_matrix.toarray().astype('float16')

    return loaded_matrix
# Load Non Similar Orga Matrix
"""
@st.cache_data
def load_nonsameorga_sim_matrix():
    loaded_matrix = load_npz("src/extended_similarities_nonsimorga.npz")
    dense_matrix = loaded_matrix.toarray().astype('float16')

    return dense_matrix
"""
def load_nonsameorga_sim_matrix():
    loaded_matrix = load_npz("src/extended_similarities_nonsimorga.npz")
    #dense_matrix = loaded_matrix.toarray().astype('float16')

    return loaded_matrix

# Load Projects DFs
@st.cache_data
def load_projects():
    orgas_df = pd.read_csv("src/projects/project_orgas.csv")
    region_df = pd.read_csv("src/projects/project_region.csv")
    sector_df = pd.read_csv("src/projects/project_sector.csv")
    status_df = pd.read_csv("src/projects/project_status.csv")
    texts_df = pd.read_csv("src/projects/project_texts.csv")

    projects_df = pd.merge(orgas_df, region_df, on='iati_id', how='inner')
    projects_df = pd.merge(projects_df, sector_df, on='iati_id', how='inner')
    projects_df = pd.merge(projects_df, status_df, on='iati_id', how='inner')
    projects_df = pd.merge(projects_df, texts_df, on='iati_id', how='inner')

    iati_search_list = [f'{row.iati_id}' for row in projects_df.itertuples()]
    title_search_list = [f'{row.title_main} ({row.orga_abbreviation.upper()})' for row in projects_df.itertuples()]

    return projects_df, iati_search_list, title_search_list

# Load CRS 3 data
@st.cache_data
def getCRS3():
    # Read in CRS3 CODELISTS
    crs3_df = pd.read_csv('src/codelists/crs3_codes.csv')
    CRS3_CODES = crs3_df['code'].tolist()
    CRS3_NAME = crs3_df['name'].tolist()
    CRS3_MERGED = {f"{name} - {code}": code for name, code in zip(CRS3_NAME, CRS3_CODES)}

    return CRS3_MERGED

# Load CRS 5 data
@st.cache_data
def getCRS5():
    # Read in CRS3 CODELISTS
    crs5_df = pd.read_csv('src/codelists/crs5_codes.csv')
    CRS5_CODES = crs5_df['code'].tolist()
    CRS5_NAME = crs5_df['name'].tolist()
    CRS5_MERGED = {code: [f"{name} - {code}"] for name, code in zip(CRS5_NAME, CRS5_CODES)}

    return CRS5_MERGED

# Load SDG data
@st.cache_data
def getSDG():
    # Read in SDG CODELISTS
    sdg_df = pd.read_csv('src/codelists/sdg_goals.csv')
    SDG_NAMES = sdg_df['name'].tolist()

    return SDG_NAMES

# Load Country Data
@st.cache_data
def getCountry():
    # Read in countries from codelist
    country_df = pd.read_csv('src/codelists/country_codes_ISO3166-1alpha-2.csv')
    COUNTRY_CODES = country_df['Alpha-2 code'].tolist()
    COUNTRY_NAMES = country_df['Country'].tolist()

    COUNTRY_OPTION_LIST = [f"{COUNTRY_NAMES[i]} ({COUNTRY_CODES[i][-3:-1].upper()})"for i in range(len(COUNTRY_NAMES))]

    return COUNTRY_OPTION_LIST

# Load Sentence Transformer Model
@st.cache_resource
def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

# Load Embeddings
@st.cache_data 
def load_embeddings_and_index():
    # Load embeddings
    with open("src/embeddings.pkl", "rb") as fIn:
        stored_data = pickle.load(fIn)
    embeddings = stored_data["embeddings"]

    return embeddings
    

# USE CACHE FUNCTIONS 
sim_matrix = load_sim_matrix()
nonsameorgas_sim_matrix = load_nonsameorga_sim_matrix()
projects_df, iati_search_list, title_search_list = load_projects()

CRS3_MERGED = getCRS3()
CRS5_MERGED = getCRS5()
SDG_NAMES = getSDG()

COUNTRY_OPTION_LIST = getCountry()

# LOAD MODEL FROM CACHE FO SEMANTIC SEARCH
model = load_model()
embeddings = load_embeddings_and_index()

def show_multi_matching_page():
    #st.write(f"Current RAM usage of this app: {get_process_memory():.2f} MB")
    #st.write(" ")
    with st.expander("Explanation"):
        st.caption("""
                    The Multi-Project Matching Feature uncovers synergy opportunities among various development banks and organizations by facilitating the search for 
                    similar projects within a selected filter setting. This innovative tool leverages an AI-driven similarity score to compare all available projects 
                    against those meeting the filter criteria, identifying potential matches that may not directly qualify under the selected filter settings. 
                    It integrates projects listed in the IATI database from leading organizations, including BMZ, KfW, GIZ, IAD, ADB, AfDB, EIB, WB, WBTF, and the German 
                    Federal Foreign Office (AA), offering a comprehensive platform for enhancing collaboration and maximizing the impact of development efforts.
                """)
        #st.write("----------------------")

    col1, col2, col3 = st.columns([10, 1, 10])
    with col1:
        st.subheader("Sector Filters (required)")
        st.caption("""
                    Sector filters must be applied to see results. The CRS5 and CRS3 classifications organise development aid into categories, 
                    with the 5-digit level providing more specific detail within the broader 3-digit categories. 
                    The SDGs are 17 UN goals that aim to achieve global sustainability, peace and prosperity by 2030. Futhermore you can Search for projects with the query field.
                    """)
    with col3:
        st.subheader("Additional Filters")
        st.caption("""
                    The additional filters allow for a more detailed search for the Multi-Project Matching.
                """)
    
    st.session_state.crs5_option_disabled = True
    col1, col2, col3 = st.columns([10, 1, 10])
    with col1:
        # CRS 3 SELECTION
        crs3_option = st.multiselect(
                        'CRS 3',
                        CRS3_MERGED,
                        placeholder="Select a CRS 3 code"
                        )

        # CRS 5 SELECTION
        ## Only enable crs5 select field when crs3 code is selected
        if crs3_option != []:
            st.session_state.crs5_option_disabled = False

        ## define list of crs5 codes dependend on crs3 codes
        crs5_list = [txt[0].replace('"', "") for crs3_item in crs3_option for code, txt in CRS5_MERGED.items() if str(code)[:3] == str(crs3_item)[-3:]]

        ## crs5 select field
        crs5_option = st.multiselect(
            'CRS 5',
            crs5_list,
            placeholder="Select a CRS 5 code",
            disabled=st.session_state.crs5_option_disabled
            )
        
        # SDG SELECTION
        sdg_option = st.selectbox(
                label = 'Sustainable Development Goal (SDG)',
                index = None,
                placeholder = "Select a SDG",
                options = SDG_NAMES[:-1],
                )

        # SEARCH BOX
        query = st.text_input("Search Query")
    
    with col3:
        # COUNTRY SELECTION
        country_option = st.multiselect(
                'Country / Countries',
                COUNTRY_OPTION_LIST,
                placeholder="All countries selected"
                )
            
        # ORGA SELECTION
        orga_abbreviation = projects_df["orga_abbreviation"].unique()
        orga_full_names = projects_df["orga_full_name"].unique()
        orga_list = [f"{orga_full_names[i]} ({orga_abbreviation[i].upper()})"for i in range(len(orga_abbreviation))]

        orga_option = st.multiselect(
                'Development Bank / Organization',
                orga_list,
                placeholder="All organizations selected"
                )
        
        different_orga_checkbox = st.checkbox("Only matches between different organizations", value=True)
        filterd_country_only_checkbox = st.checkbox("Only matches between filtered countries", value=True)


    # CRS CODE LIST
    crs3_list = [i[-3:] for i in crs3_option]
    crs5_list = [i[-5:] for i in crs5_option]

    # SDG CODE LIST
    if sdg_option != None:
        sdg_str = sdg_option.split(".")[0]
        print(sdg_str)
    else:
        sdg_str = ""

    # COUNTRY CODES LIST
    country_code_list = [option[-3:-1] for option in country_option]

    # ORGANIZATION CODES LIST
    orga_code_list = [option.split("(")[1][:-1].lower() for option in orga_option]

    # FILTER DF WITH SELECTED FILTER OPTIONS
    TOP_X_PROJECTS = 30
    filtered_df = filter_projects(projects_df, crs3_list, crs5_list, sdg_str, country_code_list, orga_code_list, query, model, embeddings, TOP_X_PROJECTS)
    if isinstance(filtered_df, pd.DataFrame) and len(filtered_df) != 0:
        # FIND MATCHES
        ## If only same country checkbox i sactivated
        if filterd_country_only_checkbox:
            with st.spinner('Please wait...'):
                compare_df = same_country_filter(projects_df, country_code_list)
        else:
            compare_df = projects_df
        
        ## if show only different orgas checkbox is activated
        if different_orga_checkbox:
            with st.spinner('Please wait...'):
                p1_df, p2_df = calc_matches(filtered_df, compare_df, nonsameorgas_sim_matrix, TOP_X_PROJECTS)
        else:
            with st.spinner('Please wait...'):
                p1_df, p2_df = calc_matches(filtered_df, compare_df, sim_matrix, TOP_X_PROJECTS)

        # SHOW THE RESULT
        show_multi_table(p1_df, p2_df)
        del p1_df, p2_df
    else:
        st.write("-----")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.write("  ")
            st.markdown("<span style='color: red'>There are no results for the applied filter. Try another filter!</span>", unsafe_allow_html=True)
        
    del crs3_list, crs5_list, sdg_str, filtered_df
    gc.collect()



def show_single_matching_page():

    with st.expander("Explanation"):
        st.caption("""
                    Single Project Matching empowers you to choose an individual project using either the project IATI ID or title, and then unveils the top 10 projects 
                    that bear the closest resemblance to your selected one. This selection is refined using a sophisticated AI algorithm that evaluates similarity based 
                    on several key dimensions: Sustainable Development Goals (SDG), Creditor Reporting System (CRS) codes, and textual analysis of project titles and 
                    descriptions. 
                    """)
        #st.write("---------")

    col1, col2 = st.columns([11, 20])
    with col1:
        st.subheader("Select a reference project")
        st.caption("""
                    Select a reference project either by its title or IATI ID to find the 10 projects most similar to it. 
                    """)
    with col2:
        st.subheader("Filters for similar projects")
        st.caption("""
                    The filters are applied to find the similar projects and are independend of the selected reference project.
                """)

    col1, col2, col3, col4 = st.columns([10, 1, 10, 10])
    with col1:
        search_option = st.selectbox(
                    label = 'Search with project title or IATI ID',
                    index = 0,
                    placeholder = " ",
                    options = ["Search with IATI ID", "Search with project title"],
                    )
        
        if search_option == "Search with IATI ID":
            search_list = iati_search_list
        else:
            search_list = title_search_list

        project_option = st.selectbox(
                    label = 'Search for a project',
                    index = None,
                    placeholder = " ",
                    options = search_list,
                    )
    
    with col3:
        # ORGA SELECTION
        orga_abbreviation = projects_df["orga_abbreviation"].unique()
        orga_full_names = projects_df["orga_full_name"].unique()
        orga_list = [f"{orga_full_names[i]} ({orga_abbreviation[i].upper()})"for i in range(len(orga_abbreviation))]

        orga_option_s = st.multiselect(
                'Development Bank / Organization ',
                orga_list,
                placeholder="All organizations selected "
                )
        
        different_orga_checkbox_s = st.checkbox("Only matches between different organizations ", value=True)

        
    with col4:
        # COUNTRY SELECTION
        country_option_s = st.multiselect(
                'Country / Countries ',
                COUNTRY_OPTION_LIST,
                placeholder="All countries selected "
                )

    st.write("--------------")

    #selected_index = None
    if project_option:
        selected_project_index = search_list.index(project_option)
        # COUNTRY CODES LIST
        country_code_list = [option[-3:-1] for option in country_option_s]

        # ORGANIZATION CODES LIST
        orga_code_list = [option.split("(")[1][:-1].lower() for option in orga_option_s]

        TOP_X_PROJECTS = 10
        with st.spinner('Please wait...'):
            filtered_df_s = filter_single(projects_df, country_code_list, orga_code_list)

        if isinstance(filtered_df_s, pd.DataFrame) and len(filtered_df_s) != 0:      
            if different_orga_checkbox_s:
                with st.spinner('Please wait...'):
                    top_projects_df = find_similar(selected_project_index, nonsameorgas_sim_matrix, filtered_df_s, 10)
            else:
                with st.spinner('Please wait...'):
                    top_projects_df = find_similar(selected_project_index, sim_matrix, filtered_df_s, 10)

            show_single_table(selected_project_index, projects_df, top_projects_df)

        else:
            st.write("-----")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st.write("  ")
                st.markdown("<span style='color: red'>Ther are no results for this filter!</span>", unsafe_allow_html=True)
            
