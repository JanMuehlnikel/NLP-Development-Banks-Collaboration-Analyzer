import streamlit as st

def show_table(data_df):
    st.write("------------------")
    
    st.dataframe(
        data_df[["title_main", "orga_abbreviation", "client", "description_main", "country", "crs_3_code", "crs_5_code"]],
        use_container_width = True,
        height = 35 + 35 * len(data_df),
        column_config={
            "orga_abbreviation": st.column_config.TextColumn(
                "Organization",
                help="If description not in English, description in other language provided",
                disabled=True
            ),
            "client": st.column_config.TextColumn(
                "Client",
                help="Client organization of customer",
                disabled=True
            ),
            "title_main": st.column_config.TextColumn(
                "Title",
                help="If title not in English, title in other language provided",
                disabled=True
            ),
            "description_main": st.column_config.TextColumn(
                "Description",
                help="If description not in English, description in other language provided",
                disabled=True
            ),
            "country": st.column_config.TextColumn(
                "Country",
                help="Country of project",
                disabled=True
            ),
            "crs_3_code": st.column_config.TextColumn(
                "CRS 3",
                help="CRS 3",
                disabled=True
            ),
            "crs_5_code": st.column_config.TextColumn(
                "CRS 5",
                help="CRS 5",
                disabled=True
            ),

        },
        hide_index=True,
    )