def total_revenue(df):

    return df["Revenue"].sum()


def daily_sales(df):

    return df.groupby("Date")["Revenue"].sum()


def hourly_sales(df):

    return df.groupby("Hour")["Revenue"].sum()


def top_products(df):

    return df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)


def top_revenue_products(df):

    return df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)


def country_sales(df):

    return df.groupby("Country")["Revenue"].sum().sort_values(ascending=False)