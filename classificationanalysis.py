import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
import numpy as np

dataset = load_breast_cancer()
print("Target Variables: ", dataset["target_names"])

(unique, counts) = np.unique(dataset["target"], return_counts=True)
print("Unique values of the target variable: ", unique)
print("Counts of the target variable: ", counts)

sns.barplot(x=dataset["target_names"], y=counts, palette="viridis")
plt.title("Target variable counts in dataset")
plt.show()