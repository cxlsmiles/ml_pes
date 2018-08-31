import h5py
import numpy as np

def load_dataset():
    dataset = h5py.File('train_examples.h5', "r")
    train_set_x_orig = np.array(dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(dataset["train_set_y"][:]) # your train set labels

    dataset = h5py.File('test_examples.h5', "r")
    test_set_x_orig = np.array(dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(dataset["test_set_y"][:]) # your test set labels
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig


def scale_array (arr, axis_):
    return (arr - np.mean(arr, axis = axis_, keepdims = True))/(np.max(arr, axis = axis_, keepdims = True) - np.min(arr, axis = axis_, keepdims = True))


def process_data(train_orig_x, train_orig_y, test_orig_x, test_orig_y):
    return scale_array(train_orig_x, 1), scale_array(train_orig_y, 1), scale_array(test_orig_x, 1), scale_array(test_orig_y, 1)
