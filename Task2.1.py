# 1.
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
# import numpy as np
# l = [12, 13, 100, 37.34]
# print("Original List:",l)
# a = np.array(l)
# print("One-dimensional NumPy array: ",a)

#######2
## Write a NumPy program to create a NumPy array with values ranging from 2 to 10.
# import numpy as np
#
# my_arr =  np.arange(2, 11)
# print("NumPy array ",my_arr)

###3
# Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
# import numpy as np
# my_arr = np.zeros(10)
# print(my_arr)
# print("Update sixth value to 11")
# my_arr[6] = 11
# print(my_arr)

####4
# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

# import numpy as np
#
# my_arr1 = np.array([0, 10, 20, 40, 3, 1,77])
# print("my_arr1: ", my_arr1)
# my_arr2 = [0, 7, 5, 56, 7, 8, 90, 40, 60, 77, 74]
# print("my_arr1: ", my_arr2)
# print("Compare each element of array1 and array2")
# print(np.in1d(my_arr1, my_arr2))