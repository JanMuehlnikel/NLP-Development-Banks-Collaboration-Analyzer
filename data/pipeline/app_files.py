"""
Create the app files 
Need to have not one big file but multiple smaller ones to stay under git 100gb limit
"""

# Dependencies
import pandas as pd

# Load merged orgas df
df = pd.read_csv("..\..\src\merged_orgas.csv")

def create_files():

    # ORGA Infos DF
    orgas_df = df[["iati_id", "iati_orga_id", "orga_abbreviation", "client","orga_full_name"]]
    orgas_df.to_csv("../../app/src/projects/project_orgas.csv", index=False)

    # Project Text (description & title)
    texts_df = df[["iati_id", "title_main", "description_main"]]
    texts_df.to_csv("../../app/src/projects/project_texts.csv", index=False)

    # Project Status DF
    status_df = df[["iati_id", "status", "planned_start", "actual_start","planned_end", "actual_end"]]
    status_df.to_csv("../../app/src/projects/project_status.csv", index=False)

    # Project region DF
    region_df = df[["iati_id", "region", "location"]]
    region_df.to_csv("../../app/src/projects/project_region.csv", index=False)

    # Project Sector DF
    sector_df = df[["iati_id", "crs_5_code", "crs_5_name", "crs_3_code", "crs_3_name", "sgd_pred_code", "sgd_pred_str"]]
    sector_df['sgd_pred_code'] = sector_df['sgd_pred_code'].astype('Int64')
    sector_df.to_csv("../../app/src/projects/project_sector.csv", index=False)

