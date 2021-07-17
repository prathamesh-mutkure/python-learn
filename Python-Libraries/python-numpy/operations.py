import numpy as np


def print_data(a, b):
    print(a + " : " + str(b))


# 0 .. 9
arr1 = np.arange(10)

# 1 .. 10
arr1 = arr1 + 1

# 10 .. 100
arr2 = arr1 * 10

print_data("arr1", arr1)
print_data("arr1 * 10", arr2)
print_data("arr2 - arr1", arr2 - arr1)
print_data("arr1 sum", arr1.sum())

