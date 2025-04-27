from numpy import where
from collections import Counter
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

#define dataset
X,y = make_blobs(n_samples=1000, centers=2, random_state=1)
print(X.shape)
print(y.shape)
counter = Counter(y)
print(counter)

#plot the dataset and give different colours for the categories
for label, _ in counter.items():
    row = where(y == label)[0]
    plt.scatter(X[row, 0], X[row, 1], label=str(label))
plt.show()