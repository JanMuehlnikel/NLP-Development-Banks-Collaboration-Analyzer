import pandas as pd

# Read merged data frame
df = pd.read_csv("app/src/crs_data.csv")

def contains_code(crs_codes, code_list):
    codes = str(crs_codes).split(';')
    return any(code in code_list for code in codes)

def calc_crs3(crs3_list: str, countries: list, orga_codes: list, show_all_countries=False, show_all_orgas = False):
    filtered_crs_df = df[df['crs_3_code'].apply(lambda x: contains_code(x, crs3_list))]

    # filter for countries
    if show_all_countries == False:
        country_filtered_df = pd.DataFrame()
        for c in countries:
            c_df = filtered_crs_df[filtered_crs_df["country"].str.contains(c, na=False)]
            country_filtered_df = pd.concat([country_filtered_df, c_df], ignore_index=True)

    # if nothing selected in st county multiselect filter with all countries 
    else:
        country_filtered_df = filtered_crs_df

    # filter for orga code
    if show_all_orgas == False:
        filtered_df = country_filtered_df[country_filtered_df['orga_abbreviation'].isin(orga_codes)]
    else:
        filtered_df = country_filtered_df
    return filtered_df

def calc_crs5(crs5_list: str, countries: list, orga_codes: list, show_all_countries=False, show_all_orgas = False):
    filtered_crs_df = df[df['crs_5_code'].apply(lambda x: contains_code(x, crs5_list))]

    # filter for countries
    if show_all_countries == False:
        country_filtered_df = pd.DataFrame()
        for c in countries:
            c_df = filtered_crs_df[filtered_crs_df["country"].str.contains(c, na=False)]
            country_filtered_df = pd.concat([country_filtered_df, c_df], ignore_index=True)
    # if nothing selected in st county multiselect filter with all countries 
    else:
        country_filtered_df = filtered_crs_df
        
    # filter for orga code
    if show_all_orgas == False:
        filtered_df = country_filtered_df[country_filtered_df['orga_abbreviation'].isin(orga_codes)]
    else:
        filtered_df = country_filtered_df

    return filtered_df

