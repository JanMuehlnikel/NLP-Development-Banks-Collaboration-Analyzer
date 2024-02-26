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

    # abbiviation gets filename
    abbreviation = org_values[1]
    # iati code the access IATI orga data
    code = org_values[2]

    fl_list = CONSTANTS.IATI_ATTRIBUTES
    fl_str = ",".join(fl_list)   
    fetch_data(KEYS.IATI_KEY, code, abbreviation, fl_str)
    transform(abbreviation)
    print(f"⯄ Finished fetching {key}.")

print("⭐ All data fetched!")







