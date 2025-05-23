
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("petrol_consumption.csv")
data.head()


y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)