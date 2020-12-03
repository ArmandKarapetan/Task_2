#####TASK2.3
# 1
# Գրել ծրագիր որը բազմաչափ NumPy զանգվածում կգտնի նրա մաքսիմում և մինիմում արժեքները
# import numpy as np
#
# x= np.array([[1.,2.,3.],[4.,5.,6.]])
# print(np.max(x),'\n',np.min(x))

##2 Գրել ծրագիր որը բազմաչափ NumPy զանգվածում կգտնի նրա մաքսիմում և մինիմում արժեքները ըստ երկրորդ սյան
# import numpy as np
#
# x= np.array([[1.,8.,3.],[4.,5.,6.]])
# print(x)
#
# print(np.max(x[1]),'\n',np.min(x[1]))

## 3 Գրել ծրագիր, որը բազմաչափ NumPy զանգվածում կգտնի նրա մեդիանան։

# import numpy as np
#
# a = [7, 2, 20, 1, 34, 10]
#
# print(a)
# print(np.median(a))
##4 Ստեղծել միաչափ և երկչափ NumPy զանգվածներ և բազմապատկեք իրար

# import numpy as np
#
# my_arry1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
# my_arr2 = np.array([0, 2, 3])
#
# print("initial array", str(my_arry1))
#
# result = my_arry1 * my_arr2 [:, np.newaxis]
#
# print("New resulting array: ", result)