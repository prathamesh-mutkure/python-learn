import numpy as np


def print_data(a, b):
    print(a + " : " + str(b))


def print_line():
    print("------------------------")


def print_array_info(arr):
    print_line()
    print(arr)
    print_line()
    print_data("shape", arr.shape)
    print_data("ndim", arr.ndim)
    print_data("dtype", arr.dtype)
    print_data("itemsize", arr.itemsize)
    print_data("size", arr.size)
    print_data("type", type(arr))


arr1 = np.arange(15).reshape(3, 5)
print_array_info(arr1)

arr2 = np.array([1, 2, 3, 4.0, 5, 6, 7, 8, 9, 10])
print_array_info(arr2)


arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print_array_info(arr3)

