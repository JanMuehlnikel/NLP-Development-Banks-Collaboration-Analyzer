import pandas as pd

# Read merged data frame
df = pd.read_csv("app/src/crs_data.csv")

def contains_code(crs_codes, code_list):
    codes = str(crs_codes).split(';')
    return any(code in code_list for code in codes)

def calc_crs3(crs3_list: str, countries: list, orga_codes: list):
    filtered_crs_df = df[df['crs_3_code'].apply(lambda x: contains_code(x, crs3_list))]

    # filter for countries
    country_filtered_df = pd.DataFrame()
    for c in countries:
        c_df = filtered_crs_df[filtered_crs_df["country"].str.contains(c, na=False)]
        country_filtered_df = pd.concat([country_filtered_df, c_df], ignore_index=True)
    
    # filter for orga code
    filtered_df = country_filtered_df[country_filtered_df['iati_orga_id'].isin(orga_codes)]

    return filtered_df

def calc_crs5(crs5_code:str, countries:list, orga_codes: list):
    # filter for crs code
    filtered_crs_df = df[df["crs_5_code"].str.contains(crs5_code, na=False)]

    # filter for countries
    country_filtered_df = pd.DataFrame()
    for c in countries:
        c_df = filtered_crs_df[filtered_crs_df["country"].str.contains(c, na=False)]
        country_filtered_df = pd.concat([country_filtered_df, c_df], ignore_index=True)
    
    # filter for orga code
    filtered_df = country_filtered_df[country_filtered_df['iati_orga_id'].isin(orga_codes)]

    return filtered_df
