import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
#from PIL import Image
from scipy import ndimage
from dnn_app_utils_v3 import *
from two_layer_nn import *
from l_layer_nn import *

np.random.seed(1)

train_orig_x, train_orig_y, test_orig_x, test_orig_y = load_data()
nx = train_orig_x.shape[1]

train_x, train_y, test_x, test_y = process_data(train_orig_x, train_orig_y, test_orig_x, test_orig_y)

m_train = train_x.shape[0]
m_test = test_x.shape[0]

# x = np.linspace(1, nx, nx)
# for i in range(m_train):
#     if i%100 == 0:
#         plt.subplot

#         plt.subplot(2, 1, 1)
#         plt.plot(x, train_x[i], 'ro')
#         plt.plot([1, nx], [train_y[0][i], train_y[0][i]])

#         plt.subplot(2, 1, 2)
#         plt.plot(x, train_orig_x[0], 'ro')
#         plt.plot([1, nx], [train_orig_y[0][0]/(2*np.pi), train_orig_y[0][0]/(2*np.pi)])
#         plt.show()

# Explore your dataset 

print ("Number of training examples: " + str(m_train))
print ("Number of testing examples: " + str(m_test))
# print ("train_x_orig shape: " + str(train_x.shape))
# print ("train_y shape: " + str(train_y.shape))
print ("test_x_orig shape: " + str(test_x.shape))
print ("test_y shape: " + str(test_y.shape))
print ("train_x's shape: " + str(train_x.shape))
print ("test_x's shape: " + str(test_x.shape))


# ## 3 - Architecture of your model

### CONSTANTS DEFINING THE MODEL ####
n_x = train_x[0].shape[0]     # num_px * num_px * 3
n_h = 7
n_y = 1
# layers_dims = (n_x, n_h, n_y)

# parameters = two_layer_model(train_x, train_y, layers_dims = (n_x, n_h, n_y), num_iterations = 5000, print_cost=True)


layers_dims = (n_x, 1400, 1400, 800, n_y)
parameters = L_layer_model(train_x, train_y, layers_dims, num_iterations = 4000, print_cost=True)

predictions_train = predict(train_x, train_y, parameters, "train")
predictions_test = predict(test_x, test_y, parameters, "test")
