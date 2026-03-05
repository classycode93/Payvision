import numpy as np
from sklearn.linear_model import LinearRegression

def revenue_prediction(daily_sales):

    daily_sales = daily_sales.reset_index()

    daily_sales["day_index"] = np.arange(len(daily_sales))

    X = daily_sales[["day_index"]]

    y = daily_sales["Revenue"]

    model = LinearRegression()

    model.fit(X, y)

    next_day = np.array([[len(daily_sales)]])

    prediction = model.predict(next_day)

    return prediction[0]