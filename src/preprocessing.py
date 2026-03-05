import pandas as pd

def clean_data(df):

    # remove missing customers
    df = df.dropna(subset=["CustomerID"])

    # remove cancelled orders
    df = df[df["Quantity"] > 0]

    # convert date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # create revenue column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # extract hour and date
    df["Hour"] = df["InvoiceDate"].dt.hour
    df["Date"] = df["InvoiceDate"].dt.date

    return df