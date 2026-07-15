import pandas as pd

from src.database import engine


def load_data(transaction):

    df = pd.DataFrame([transaction])

    df.to_sql(
        "financial_transactions",
        engine,
        if_exists="append",
        index=False
    )