"""
Method to transform and engineer reponse csv's to data frame and save them as csv
The transformation process can be viewed in more detail as jupyter notebook in notebooks/transformation_json
"""

# DEPENDENCIES
import pandas as pd
import numpy as np
from sdg_pred import pred_sdg

def transform(abbreviation:str, iati_orga_id:str, orga_full_name:str):

    # Set PARAMS
    response_folder = "../../src/responses/"
    transformed_folder = "../../src/transformed/"
    response_file = response_folder + f"response_{abbreviation}.json" # json format -> fetched in iati.ipynb
    output_file = transformed_folder + f"transformed_{abbreviation}.csv" # save df as csv


    #Read in data into df from json
    df = pd.read_json(response_file)
    print(f"⮩ {abbreviation} with entries: {len(df)}")

    # create new empty df to fill with transformed data
    trans_df = pd.DataFrame()

    def iati_id(trans_df):
        trans_df["iati_id"] = df["iati_identifier"].values

    def iati_orga_ids(trans_df):
        trans_df["iati_orga_id"] = iati_orga_id
        trans_df["orga_abbreviation"] = abbreviation
        trans_df["orga_full_name"] = orga_full_name

    def project_number(trans_df):
        try:
            project_number = iati_orga_id.split("-")[1]

            trans_df["project_number"] = project_number
        except:
            trans_df["project_number"] = "NaN"

    def en_title(trans_df):
        trans_df["title_en"] = "NaN"

        for index, row in df.iterrows():
            title_row = row['title_narrative']
            try:
                if 'title_narrative_xml_lang' in df.columns:
                    lang_list = row['title_narrative_xml_lang']

                    # nan in pandas is type float
                    # check if nan and if yes take first entry in lang
                    if isinstance(lang_list, float):
                        if isinstance(title_row, float):
                            trans_df["title_en"][index] = "NaN"
                        else:
                            trans_df["title_en"][index] = title_row[0]
                    elif len(lang_list) == len(title_row):
                        for j in range(0, len(lang_list)):
                            if "en" or "EN" in lang_list:
                                if lang_list[j].lower() == "en":
                                    title = title_row[j]
                                    trans_df["title_en"][index] = title
                            else:
                                trans_df["title_en"][index] = "NaN"
                    else:
                        pass
                else:
                    trans_df["title_en"][index] = row['title_narrative'][0]
            except:
                print(f"Error: Index: {index}, Row: {lang_list}, {title_row}")

    def other_title(trans_df):
        trans_df["title_other"] = "NaN"

        for index, row in df.iterrows():
            title_row = row['title_narrative']
            try:
                if 'title_narrative_xml_lang' in df.columns:
                    lang_list = row['title_narrative_xml_lang']

                    # every title which is has no lang attribute is classified as English and therefore not in other
                    if isinstance(lang_list, float):
                        trans_df["title_other"][index] = "NaN"
                    elif len(lang_list) == len(title_row):
                        for j in range(0, len(lang_list)):
                            if lang_list[j].lower() != "en":
                                title = row['title_narrative'][j]
                                if trans_df["title_other"][index] == "NaN":
                                    trans_df["title_other"][index] = title
                                else:
                                    trans_df["title_other"][index] = f"{trans_df['title_other'][index]}; {title}"
                    else:
                        trans_df["title_other"][index] = title
                    

                else:
                    trans_df["title_other"][index] = "NaN"
                
            except Exception as e:
                print(f"Error: Index: {index} \n Row: {row} \n Exception: {e}")
    
    def main_title(trans_df):
        trans_df['title_main'] = trans_df["title_en"]
        trans_df.loc[trans_df['title_main'] == "NaN", 'title_main'] = trans_df['title_other']

    def organization(trans_df):
        trans_df['organization'] = df['reporting_org_narrative'].apply(lambda x: x[0])

    def country(trans_df):
        trans_df["country_code"] = df["recipient_country_code"]
        trans_df["country"] = "NaN"

        for index, row in df.iterrows():
            country_list = row["recipient_country_code"]

            if isinstance(country_list, float):
                trans_df["country"][index] = "NaN"
            else:
                country_str = ""
                for i in country_list:
                    country_str += f"{i}; "
                
                trans_df["country"][index] = country_str

    def region(trans_df):
        trans_df['region'] = df['recipient_region_code']

    def location(trans_df):
        try: 
            if 'title_narrative_xml_lang' in df.columns:
                trans_df['location'] = df['location_name_narrative']
            else:
                trans_df['location'] = "NaN"
        except:
                trans_df['location'] = "NaN"  

    def description(trans_df):
        trans_df["description_en"] = "NaN"
        trans_df["description_other"] = "NaN"

        for index, row in df.iterrows():

            try:
                if 'description_narrative_xml_lang' in df.columns:
                    descr_list = row['description_narrative_xml_lang'] # list with languages provided 
                    descr_row = row['description_narrative'] # list with the despription narrative of all languages provided

                    # nan in pandas is type float
                    # check if nan and if yes take first entry in descr
                    if isinstance(descr_list, float):
                        if isinstance(descr_row, float):
                            trans_df["description_en"][index] = "NaN"
                        else:
                            trans_df["description_en"][index] = descr_row[0]
                    else:
                        if len(descr_list) == len(descr_row):
                            descr_len = len(descr_list)
                        else:
                            descr_len = len(descr_row)
                        # iterate throug description list
                        for j in range(0, descr_len):
                            # if description english
                            if descr_list[j].lower() == "en":
                                if type(descr_row) == float:
                                    descr = "NaN"
                                else:
                                    descr = descr_row[j]
                                if trans_df["description_en"][index] == "NaN":
                                    trans_df["description_en"][index] = descr
                                else:
                                    trans_df["description_en"][index] = f"{trans_df['description_en'][index]}; {descr}"
                            else:
                                if type(descr_row) == float:
                                    descr = "NaN"
                                else:
                                    descr = descr_row[j]
                                if trans_df["description_other"][index] == "NaN":
                                    trans_df["description_other"][index] = descr
                                else:
                                    trans_df["description_other"][index] = f"{trans_df['description_other'][index]}; {descr}"
                else:
                    descr_str = ""
                    for d in row['description_narrative']:
                        descr_str += f"{d}; "
                    trans_df["description_en"][index] = descr_str

            except Exception as e:
                #print(e)
                #print(f"Error: Index: {index} \n Row: {row}")
                pass

    def main_description(trans_df):
        trans_df['description_main'] = trans_df.description_en
        trans_df.loc[trans_df['description_main'] == "NaN", 'description_main'] = trans_df['description_other']

    def status(trans_df):
        activity_status = {
            1: "Pipeline/identification",
            2: "Implementation",
            3: "Finalisation",
            4: "Closed",
            5: "Cancelled",
            6: "Suspended"
        }

        trans_df["status"] = df.activity_status_code
        trans_df['status'] = trans_df['status'].replace(activity_status)

    def date(trans_df):
        # One Hot
        # 1 -> Yes
        # 0 -> No

        # Codes:
        # 1 Planned start
        # 2 Actual start
        # 3 Planned end
        # 4 Actual end

        trans_df["planned_start"] = "NaN"
        trans_df["actual_start"] = "NaN"
        trans_df["planned_end"] = "NaN"
        trans_df["actual_end"] = "NaN"

        date_types = {
            1: "planned_start",
            2: "actual_start",
            3: "planned_end",
            4: "actual_end"
        }

        for index, row in df.iterrows():
            dtype_list = row["activity_date_type"]
            iso_date_list = row["activity_date_iso_date"]

            combined_list = list(zip(dtype_list, iso_date_list))

            # replace nums with column names from date_types
            combined_list = [(date_types[int(t[0])], t[1]) for t in combined_list]

            for i in combined_list:
                trans_df[i[0]] = i[1]

    def last_update(trans_df):
        trans_df['last_update'] = df['last_updated_datetime']

    def sector_codes(trans_df):
        sector_codes = {
            1: "OECD DAC CRS Purpose Codes (5 digit)",
            2: "OECD DAC CRS Purpose Codes (3 digit)",
            3: "Classification of the Functions of Government (UN)",
            4: "Statistical classification of economic activities in the European Community",
            5: "National Taxonomy for Exempt Entities (USA)",
            6: "AidData",
            7: "SDG Goal",
            8: "SDG Target",
            9: "SDG Indicator",
            10: "Humanitarian Global Clusters (Inter-Agency Standing Committee)",
            11: "North American Industry Classification System (NAICS)",
            12: "UN System Function",
            99: "Reporting Organisation", # The sector reported corresponds to a sector vocabulary maintained by the reporting organisation for this activity
            98: "Reporting Organisation 2" # The sector reported corresponds to a sector vocabulary maintained by the reporting organisation for this activity (if they are referencing more than one)
        }

        crs5_df = pd.read_csv("../../src/codelists/crs5_codes.csv")
        crs3_df = pd.read_csv("../../src/codelists/crs3_codes.csv")

        # helper functions for sector codes
        def process_codes(combined_list, translation_df, code_index):
            code_text = ""
            codes_nums = ""
            if any(item[0] == code_index for item in combined_list):
                for i in combined_list:
                    if i[0] == code_index:
                        translation = translation_df.loc[translation_df['code'] == int(i[1]), 'name'].values[0]
                        code_text += f"{translation}; "
                        codes_nums += f"{i[1]}; "
                return code_text, codes_nums
            else:
                return "NaN", "NaN"
            
        def derive_crs3(combined_list, translation_df, code_index="1"):
            code_text = ""
            codes_nums = ""
            if any(item[0] == code_index for item in combined_list):
                for i in combined_list:
                    if i[0] == code_index:
                        translation = translation_df.loc[translation_df['code'] == int(i[1][:3]), 'name'].values[0]
                        code_text += f"{translation}; "
                        codes_nums += f"{i[1][:3]}; "
                return code_text, codes_nums
            else:
                return "NaN", "NaN"

        #Extract CRS5 codes and derive crs3 codes from crs5 codes
        trans_df["crs_5_code"] = "NaN"
        trans_df["crs_5_name"] = "NaN"

        # Most Project dont have information on crs3 -> crs3 derived from crs5 tags
        trans_df["crs_3_code"] = "NaN"
        trans_df["crs_3_name"] = "NaN"


        for index, row in df.iterrows():
            crs_voc_list = row['sector_vocabulary']
            crs_code_list = row['sector_code']

            if type(crs_voc_list) == float:
                pass
            else:
                try:
                    combined_list = list(zip(crs_voc_list, crs_code_list))

                    # CRS 5
                    crs5_str, crs5_codes = process_codes(combined_list, crs5_df, "1")
                    trans_df["crs_5_code"][index] = crs5_codes
                    trans_df["crs_5_name"][index] = crs5_str
                    
                    # CRS 3
                    crs3_str, crs3_codes = derive_crs3(combined_list, crs3_df)
                    trans_df["crs_3_code"][index] = crs3_codes
                    trans_df["crs_3_name"][index] = crs3_str

                except:
                    print(f"Error on Index {index}, {crs_code_list}")
                    pass

    def documents(trans_df):
        try:
            trans_df['docs'] = df['document_link_url']
        except:
            trans_df["docs"] = "NaN" 

    iati_id(trans_df)
    iati_orga_ids(trans_df)
    #project_number(trans_df)
    en_title(trans_df)
    other_title(trans_df)
    main_title(trans_df)
    organization(trans_df)
    country(trans_df)
    region(trans_df)
    location(trans_df)
    description(trans_df)
    main_description(trans_df)
    status(trans_df)
    date(trans_df)
    last_update(trans_df)
    sector_codes(trans_df)
    documents(trans_df)

    # comment out if a prediction of sdg is not wished
    pred_sdg(trans_df)

    # export df as csv to src/transformed/
    trans_df.to_csv(output_file, index=False) 
    print(f"⮩ Final {abbreviation} is saved in src/transformed/")


