# -*- coding: utf-8 -*-
"""Simple_Linear_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qf5ynIWk1WgF2vzAOagJ791I-gWMQuKu

#Linear Regression works only with the dataset that has only one column

#Import Necessary Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""#Import the dataset"""

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Machine_Learning/Datasets/salary_data.csv')

df.shape

df.head()

#All columns except the last (Target) are selected.
X = df.iloc[:, :-1].values #Selects all rows (:) and all columns except the last one (:-1)

#Extract the target variable (y) from a dataset
y = df.iloc[:, -1].values #Selects all rows (:) and only the last column (-1) (target variable)

"""#Split into Training set and Testing set"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

X_train.shape

y_train.shape

"""#Dimension Matching"""

# Select a single feature (e.g., first column)
X_feature = X_train[:, 0].reshape(-1, 1)  # Reshape for sklearn

# Ensure y_train is the correct shape
y_train = y_train.reshape(-1, 1)

"""#Training Simple Linear Regression model on Training set"""

from sklearn.linear_model import LinearRegression

# model creation and training
model = LinearRegression()
model.fit(X_train, y_train)

"""#Predicting Test set"""

y_pred = model.predict(X_test)

"""#Training set Visualization"""

plt.scatter(X_train, y_train, color = 'red') ## input data
plt.plot(X_train, model.predict(X_train), color = 'blue') ## visualize regressor line
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""#Testing set Visualization"""

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()