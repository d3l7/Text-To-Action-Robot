from keras.datasets import mnist
import matplotlib.pyplot as plt
(X_train,y_train), (X_test, y_test)= mnist.load_data()
#X_train is a 3d array with 60000 being the first value and the number of elements
#Y train is a 1d array containing 60000 elements and indexes X train so you know what each image is what number
#X and y test are the same as train but only with 10000 elements
plt.subplot()
plt.imshow(X_train[9], cmap=plt.get_cmap('gray'))

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np

# number_pix=X_train.shape[1]*X_train.shape[2]
# print(f"{X_train.shape[0]}\n {X_train.shape[1]}")
# X_train=X_train.reshape(X_train.shape[0], number_pix).astype('float32')
# X_test=X_test.reshape(X_test.shape[0], number_pix).astype('float32')
# print(f"{X_train.shape[0]}\n {X_train.shape[1]}")