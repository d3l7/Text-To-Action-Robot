from keras.datasets import mnist
import matplotlib.pyplot as plt
(X_train,y_train), (X_test, y_test)= mnist.load_data()
#X_train is a 3d array with 60000 being the first value and the number of elements
#Y train is a 1d array containing 60000 elements and indexes X train so you know what each image is what number
#X and y test are the same as train but only with 10000 elements
plt.subplot()
plt.imshow(X_train[9], cmap=plt.get_cmap('gray'))

#Importing modules (np utils is imported seperately instead of being a part of keras.utils)
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
#import np_utils
from keras import utils as np_utils

number_pix=X_train.shape[1]*X_train.shape[2]
X_train=X_train.reshape(X_train.shape[0], number_pix).astype('float32')
X_test=X_test.reshape(X_test.shape[0], number_pix).astype('float32')
#X_train and test have been reshaped to be the number of items (60000)
#Also number of pixels all in a 2d array (784)

X_train=X_train/255
X_test=X_test/255
#Y_train and test have become 2d from 1d (vector to matrix)
#With the second value being how many different values there can be (classes)
#This function (to categorical) returns a matrix of binary values (either ‘1’ or ‘0’). 
#It has number of rows equal to the length of the input vector and number of columns
#Equal to the number of classes.
y_train= np_utils.to_categorical(y_train)
y_test= np_utils.to_categorical(y_test)
num_classes=y_train.shape[1]

def nn_model():
    model=Sequential()
    model.add(Dense(number_pix, input_dim=number_pix, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimiser='Adam', metrics=['accuracy'])
    return model

print(nn_model())