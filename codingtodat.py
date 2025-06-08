from sklearn.linear_model import LogisticRegression
from sklearn import datasets


iris = datasets.load_iris()
X = iris.data[:, :2] #we take only the first two features
Y = iris.target

# data = sns.load_dataset("iris")
# data.head()
#train the model
logreg = LogisticRegression(multi_class="multinomial")
logreg.fit(X, Y)

x_min, x_max =X[:, 0].min() -. 5,X[:,0].max() -. 5
y_min, y_max = x[:, 1].min() - .5, x[:, 1].max() -. 5
h = 0.2 #step size of the mesh

xx, yy = np.meshgrid(np.arange(x_min,x_max, h),
np.arange(y_min, y_max, h))

#X[:, :0] => gets all the values of the first feature
#.min() => samallest values of the first feature(sepal_length)
#.max() => miaximum value of the first feature

z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])
Z = z.reshape(xx.shape)