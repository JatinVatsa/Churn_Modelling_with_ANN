# Artifical Neural Networks (ANN)

# Part 1 Data preprocessing

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing data set
dataset = pd.read_csv('Churn_Modelling.csv')
X=dataset.iloc[:,3:-1].values  
Y=dataset.iloc[:,-1].values

#encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
label=LabelEncoder()
X[:,1]=label.fit_transform(X[:,1])
X[:,2]=label.fit_transform(X[:,2])
ct=ColumnTransformer([('Geography',OneHotEncoder(),[1])],remainder='passthrough')
X=ct.fit_transform(X) 

#avoiding dummy variable trap
X=X[:,1:]
X=np.array(X,dtype=float)


#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

#feature scaling it is imp in neural network
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)




# Part 2 - Now lets make ANN!
# importing the keras library & packages
import keras 
from keras.models import Sequential
from keras.layers import Dense

#initialsing the ANN
classifier= Sequential()

# adding the i/p layer & first hidden layer
classifier.add(Dense(units = 6, kernel_initializer ='uniform', activation='relu', input_dim= 11))

# adding the second layer
classifier.add(Dense(units = 6, kernel_initializer ='uniform', activation='relu'))

# adding the o/p layer
classifier.add(Dense(units = 1, kernel_initializer ='uniform', activation='sigmoid')) # for o/p layer we use sigmoid fun for finding probability

# Compiling the ANN i.e applying stochastic gradient descent method
classifier.compile(optimizer='adam',loss='binary_crossentropy', metrics= ['accuracy'])

# fiiting the ANN to the training set
classifier.fit(X_train,Y_train, batch_size = 10, epochs= 100)



# Part 3 Making the predictions & evaluating the model

#predicting test  set result
y_pred=classifier.predict(X_test) 
y_pred = (y_pred > 0.5)  # it is equalient to if y_pred > 50%  it return true ,else false

# making the confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,y_pred)