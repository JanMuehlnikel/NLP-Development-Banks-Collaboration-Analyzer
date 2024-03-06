import pandas as pd

# Read merged data frame
df = pd.read_csv("src/merged_orgas.csv")

def calc_crs3(crs3_code: str, countries: list):
    filtered_crs_df = df[df["crs_3_code"].str.contains(crs3_code, na=False)]
    filtered_df = pd.DataFrame()
    for c in countries:
        c_df = filtered_crs_df[filtered_crs_df["country"].str.contains(c, na=False)]
        filtered_df = filtered_df.append(c_df, ignore_index=True)

    return filtered_df

def calc_crs5(crs5_code:str, countries:list):
    filtered_crs_df = df[df["crs_5_code"].str.contains(crs5_code, na=False)]
    filtered_df = pd.DataFrame()
    for c in countries:
        c_df = filtered_crs_df[filtered_crs_df["country"].str.contains(c, na=False)]
        filtered_df = filtered_df.append(c_df, ignore_index=True)

    return filtered_df
