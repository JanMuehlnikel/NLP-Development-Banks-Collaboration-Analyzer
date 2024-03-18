"""
Page for similarities
"""

################
# DEPENDENCIES #
################
import streamlit as st
import pandas as pd
from scipy.sparse import load_npz
import utils.similarity_table as similarity_table

# Catch DATA
# Load Similarity matrix
@st.cache_data
def load_sim_matrix():
    loaded_matrix = load_npz("app/src/similarities.npz")
    dense_matrix = loaded_matrix.toarray()


    return dense_matrix


@st.cache_data
def load_projects():
    orgas_df = pd.read_csv("app/src/projects/project_orgas.csv")
    region_df = pd.read_csv("app/src/projects/project_region.csv")
    sector_df = pd.read_csv("app/src/projects/project_sector.csv")
    status_df = pd.read_csv("app/src/projects/project_status.csv")
    texts_df = pd.read_csv("app/src/projects/project_texts.csv")

    projects_df = pd.merge(orgas_df, region_df, on='iati_id', how='inner')
    projects_df = pd.merge(projects_df, sector_df, on='iati_id', how='inner')
    projects_df = pd.merge(projects_df, status_df, on='iati_id', how='inner')
    projects_df = pd.merge(projects_df, texts_df, on='iati_id', how='inner')

    return projects_df

# LOAD DATA
sim_matrix = load_sim_matrix()
projects_df = load_projects()

def show_page():
    st.write("Similarities")

    df_subset = projects_df.head(10)
    selected_index = st.selectbox('Select an entry', df_subset.index, format_func=lambda x: df_subset.loc[x, 'iati_id'])

    st.write(selected_index)

    # add index and similarity together
    indecies = range(0, len(sim_matrix))
    similarities = sim_matrix[selected_index]
    zipped_sims = list(zip(indecies, similarities))

    # remove all 0 similarities
    filtered_sims = [(index, similarity) for index, similarity in zipped_sims if similarity != 0]

    # Select and sort top 20 most similar projects
    sorted_sims = sorted(filtered_sims, key=lambda x: x[1], reverse=True)
    top_20_sims = sorted_sims[:20]

    # create result data frame
    index_list = [tup[0] for tup in top_20_sims]
    print(index_list)
    result_df = projects_df.iloc[index_list]
    print(len(result_df))

    print(len(result_df))
    # add other colums to result df

    similarity_list = [tup[1] for tup in top_20_sims]
    result_df["similarity"] = similarity_list

    similarity_table.show_table(result_df, similarity_list)
    
    

