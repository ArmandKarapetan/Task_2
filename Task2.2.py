###TASK2.2
# 1.
# Write a NumPy program to compute the multiplication of two given matrixes

# import numpy as np
#
# x = np.array([[10., 7., 3.], [4., 5., 77.]])
# y = np.array([[7., 45.], [-1, 7], [10, 9]])
#
# mul_res = x.dot(y)
# print("MUltiply result", '\n', mul_res, '\n')

#####2.
##Write a NumPy program to compute the determinant of an array

# import numpy as np
#
# x = np.array([[10., 7., 3.], [4., 5., 77.]])
#
# from numpy.linalg import inv, qr
#
# mat = x.T.dot(x)
#
# print('multiply with transpose')
# print(mat, '\n')

###3.
### Write a NumPy program to compute the sum of the diagonal element of a given array

# import numpy as np
#
# x = np.array([[10., 7., 3.], [4., 5., 77.]])
# result = np.trace(x)
# print(result)

##4
###Write a NumPy program to compute the inverse of a given matrix
# import numpy as np
#
# x = np.array([[10, 3], [4, 5]])
#
# inv_result = np.linalg.inv(x)
# print(inv_result)

##5
###Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.
# import numpy as np
#
# x = np.array([[10, 3], [4, 5]])
#
# np.save("File name",x)
# read_file= np.load("File name.npy")
# print(read_file)
