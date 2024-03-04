"""
Method to predict Sustainable Development Goals with the description
"""

###############
# Dependecies #
###############
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import pandas as pd
import numpy as np



def pred_sdg(df):
    print("Debugger: Pred started")
    # Load model and tokenizer: https://huggingface.co/jonas/sdg_classifier_osdg
    model = AutoModelForSequenceClassification.from_pretrained("jonas/sdg_classifier_osdg", use_auth_token="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")
    tokenizer = AutoTokenizer.from_pretrained("jonas/sdg_classifier_osdg", use_auth_token="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")

    # Load sdg codelist df
    sdg_df = pd.read_csv("../../src/codelists/sdg_goals.csv")

    # Define sdg columns 
    df["sgd_pred_code"] = "NaN"
    df["sgd_pred_str"] = "NaN"

    # Iterate through df and predict sdg

    fulll_len_df = len(df)
    for index, row in df.iterrows():
        print(f"{index} / {fulll_len_df}")
        descr_row = row['description_main']
        try:
            # nan in pandas is type float
            # check if nan 
                if isinstance(descr_row, float):
                    df["sgd_pred_code"][index] = "NaN"
                    df["sgd_pred_str"][index] = "NaN"
                else:
                    if len(descr_row) > 512:
                        descr_row = descr_row[:512]
                    # use clf with description and predict sgd 
                    inputs = tokenizer(descr_row, return_tensors="pt")
                    sdg_pred = model(**inputs)

                    # etxract the argmax of the sgd pred
                    # extract the sgd wich is most probable
                    sdg_tuple = sdg_pred.to_tuple()
                    sdg_np = sdg_tuple[0][0].detach().numpy()
                    sdg_code = sdg_np.argmax() + 1

                    # Map sgd codes to names
                    sdg_translation = sdg_df.loc[sdg_df['code'] == int(sdg_code), 'name'].values[0]

                    df["sgd_pred_code"][index] = sdg_code
                    df["sgd_pred_str"][index] = sdg_translation
        except Exception as e:
            print(f"{e}: {descr_row}")


    print("Debugger: Pred finished")