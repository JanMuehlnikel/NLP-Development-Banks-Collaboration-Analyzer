import pandas as pd

# Read merged data frame
df = pd.read_csv("src/merged_orgas.csv")

# Function to calculate crs3 & country overlaps 
def calc_crs3(crs3_code:str, country):
    filtered_country_df = df[df["crs_3_code"].str.contains(crs3_code, na=False)]
    filtered_df = filtered_country_df[filtered_country_df["country"].str.contains(country, na=False)]

    return filtered_df

def calc_crs5(crs5_code:str, country):
    filtered_country_df = df[df["crs_5_code"].str.contains(crs5_code, na=False)]
    filtered_df = filtered_country_df[filtered_country_df["country"].str.contains(country, na=False)]

    return filtered_df
