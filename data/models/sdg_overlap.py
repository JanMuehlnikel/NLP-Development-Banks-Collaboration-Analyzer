import pandas as pd

# Read merged data frame
df = pd.read_csv("app/src/sdg_data.csv")

def calc_crs3(sdg_int: str, countries: list, orga_codes: list, show_all_countries=False, show_all_orgas = False):
    # filter for sdg code
    filtered_sdg_df = df[df["sgd_pred_code"] == sdg_int]

    # filter for countries
    if show_all_countries == False:
        country_filtered_df = pd.DataFrame()    
        for c in countries:
            c_df = filtered_sdg_df[filtered_sdg_df["country"].str.contains(c, na=False)]
            country_filtered_df = pd.concat([country_filtered_df, c_df], ignore_index=True)
    else:
        country_filtered_df = filtered_sdg_df
    
    # filter for orga code
    if show_all_orgas == False:
        filtered_df = country_filtered_df[country_filtered_df['orga_abbreviation'].isin(orga_codes)]
    else:
        filtered_df = country_filtered_df

    return filtered_df