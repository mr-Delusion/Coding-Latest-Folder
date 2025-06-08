import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("insurance_data.csv")
df.head()

plt.scatter(df.age, df.bought_insurance, marker="+", color="red")
plt.show()