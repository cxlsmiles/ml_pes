import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.framework import ops
from dnn_uitls import *

train_orig_x, train_orig_y, test_orig_x, test_orig_y = load_dataset()

train_x, train_y, test_x, test_y = process_data(train_orig_x, train_orig_y, test_orig_x, test_orig_y)

