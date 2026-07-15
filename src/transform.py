import pandas as pd

def transform_data(transaction):

    df = pd.DataFrame([transaction])

    df["amount"] = df["amount"].round(2)

    return df