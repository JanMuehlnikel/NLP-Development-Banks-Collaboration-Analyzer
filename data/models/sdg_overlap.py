import pandas as pd

# Read merged data frame
df = pd.read_csv("app/src/sdg_data.csv")

def calc_crs3(sdg_int: str, countries: list, orga_codes: list):
    # filter for sdg code
    filtered_sdg_df = df[df["sgd_pred_code"] == sdg_int]

    # filter for countries
    country_filtered_df = pd.DataFrame()
    for c in countries:
        c_df = filtered_sdg_df[filtered_sdg_df["country"].str.contains(c, na=False)]
        country_filtered_df = pd.concat([country_filtered_df, c_df], ignore_index=True)
    
    # filter for orga code
    filtered_df = country_filtered_df[country_filtered_df['iati_orga_id'].isin(orga_codes)]

    return filtered_df