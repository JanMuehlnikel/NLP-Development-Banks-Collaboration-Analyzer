"""
Create the app files 
Need to have not one big file but multiple smaller ones to stay under git 100gb limit
"""

# Dependencies
import pandas as pd

# Load merged orgas df
df = pd.read_csv("..\..\..\src\merged_orgas.csv")

def create_files():

    # CREATE CRS DF
    crs_df = df[["iati_id", "orga_abbreviation", "orga_full_name", "title_main", "country", "description_main", "status", "crs_5_code", "crs_3_code"]]
    crs_df.to_csv("../../app/src/crs_data.csv", index=False)

    # CREATE SDG DF
    sdg_df = df[["iati_id", "iati_orga_id", "orga_abbreviation", "orga_full_name", "title_main", "country", "description_main", "status", "sgd_pred_code"]]
    sdg_df['sgd_pred_code'] = sdg_df['sgd_pred_code'].astype('Int64')

    sdg_df.to_csv("../../app/src/sdg_data.csv", index=False)
