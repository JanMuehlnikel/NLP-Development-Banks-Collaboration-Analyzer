"""
Method to merga all organizational csv files to one containing all data
"""

###############
# Dependecies #
###############
import pandas as pd

# Your current dirctory has to be /data/pipeline/ to not get FileNotFoundError
from importlib.machinery import SourceFileLoader
CONSTANTS = SourceFileLoader("CONSTANTS", "../../config/CONSTANTS.py").load_module()

# Merge all organization csv's
def merge():
    combined_df = pd.DataFrame()

    for key, values in CONSTANTS.ORGANIZATIONS.items():
        path = f"../../../src/transformed/transformed_{values[1]}.csv"

        temp_df = pd.read_csv(path)
        combined_df = pd.concat([combined_df, temp_df], ignore_index=True)

    combined_df.to_csv("../../../src/merged_orgas.csv", index=False)