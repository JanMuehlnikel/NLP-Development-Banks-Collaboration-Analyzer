"""
Method to predict Sustainable Development Goals with the description
"""

###############
# Dependecies #
###############
from transformers import pipeline
import pandas as pd
from tqdm import tqdm


def pred_sdg(df):
    print("Debugger: Pred started")
    # Load model: https://huggingface.co/jonas/sdg_classifier_osdg
    pipe = pipeline("text-classification", model="jonas/roberta-base-finetuned-sdg")

    # Load sdg codelist df
    sdg_df = pd.read_csv("../../src/codelists/sdg_goals.csv")

    # Define sdg columns 
    df["sgd_pred_code"] = "NaN"
    df["sgd_pred_str"] = "NaN"

    len_df = len(df)

    for index, row in tqdm(df.iterrows(), total=len_df, desc="Processing"):
        if index % 500 == 0:
            print(f" Debugger: {index} / {len_df}")
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
                    pred = pipe(descr_row)
                    pred_str = pred[0]["label"]
                    pred_int = int(pred_str)

                    # Map sgd codes to names
                    sdg_translation = sdg_df.loc[sdg_df['code'] == pred_int, 'name']

                    df["sgd_pred_code"][index] = pred_int
                    df["sgd_pred_str"][index] = sdg_translation
        except Exception as e:
            print(f"Error {e}: {descr_row}")


    print("Debugger: Pred finished")