import pandas as pd

def load_data(path):

    df = pd.read_excel("data\Online Retail.xlsx")

    return df