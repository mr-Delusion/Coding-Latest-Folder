import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


#load diabetes dataset
diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)

#Use only one feature
diabetes_x = diabetes_x[:, np.newaxis, 2]

#splitting the data into training and testing sets
diabetes_x_train = diabetes_x[:-20] #all the data except the last 20
diabetes_x_test = diabetes_x[-20:] #the last 20 values

#splittng the data into testing and training
diabetes_y_train = diabetes_y[:-20] #all the data except the last 20 values
diabetes_y_test = diabetes_y[-20:] #the last 20 values

#Create a linear regression model
regr = linear_model.LinearRegression()

#training the machine/model
regr.fit(diabetes_x_train, diabetes_y_train)

#make predictions
diabetes_y_pred = regr.predict(diabetes_x_test)

#plot
plt.scatter(diabetes_x_test, diabetes_y_test)
plt.plot(diabetes_x_test, diabetes_y_pred, color='red', linewidth=3)
plt.show()