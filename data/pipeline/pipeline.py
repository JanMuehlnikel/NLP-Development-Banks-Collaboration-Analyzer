"""
This file contains a pipeline which can be used to extract all organizational data and transfrom it into a data frame

1. Get data from IATI datastore API
2. Save orga json in src/responses/
3. Transofrom json file into data frame format and engineer features
4. Export transformed orga data as csv into src/transformed
"""

###############
# Dependecies #
###############
from fetch_api import fetch_data
from transform import transform
from merge_csv import merge
from app_files import create_files
import pandas as pd
import warnings

# Ignore SettingWithCopyWarning
warnings.filterwarnings('ignore', module='pandas')


# Your current dirctory has to be /data/pipeline/ to not get FileNotFoundError
from importlib.machinery import SourceFileLoader
CONSTANTS = SourceFileLoader("CONSTANTS", "../../config/CONSTANTS.py").load_module()
KEYS = SourceFileLoader("KEYS", "../../config/KEYS.py").load_module()
# Iterate through all organizations
for key, org_values in CONSTANTS.ORGANIZATIONS.items():
    print(f"⯈ Start fetching {key}.")

    #################################
    # Fetch data with datastore API #
    #################################
    
    # get features to fetch
    fl_list = CONSTANTS.IATI_ATTRIBUTES
    fl_str = ",".join(fl_list)   

    # fetch abbreviation, fullname and IATI Oraganization ID from CONSTANTS.py to use in pipeline
    abbreviation = org_values[1] # abbiviation becomes the filename
    orga_full_name = org_values[0] 
    iati_org_id = org_values[2]


    fl_list = CONSTANTS.IATI_ATTRIBUTES
    fl_str = ",".join(fl_list)   
    fetch_data(KEYS.IATI_KEY, iati_org_id, abbreviation, fl_str)
    transform(abbreviation, iati_org_id, orga_full_name)
    print(f"⯄ Finished fetching {key}.")

merge()
create_files()

print("⭐ All data fetched!")
