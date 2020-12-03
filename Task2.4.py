######TASK 2.4
# 1 Write a Pandas program to add, subtract, multiple and divide two Pandas Series

# import pandas as pd
# ds1 = pd.Series([2, 4, 6, 8, 10])
# ds2 = pd.Series([1, 3, 5, 7, 9])
# ds = ds1 + ds2
# print("Add two Series:")
# print(ds)
# print("Subtract two Series:")
# ds = ds1 - ds2
# print(ds)
# print("Multiply two Series:")
# ds = ds1 * ds2
# print(ds)
# print("Divide Series1 by Series2:")
# ds = ds1 / ds2
# print(ds)

#####2 Write a Pandas program to convert a dictionary to a Pandas series.

# import pandas as pd
# d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
# print("Original dictionary:")
# print(d1)
# new_series = pd.Series(d1)
# print("Converted series:")
# print(new_series)


####3
# Write a Pandas program to convert a NumPy array to a Pandas series
# import numpy as np
# import pandas as pd
# np_array = np.array([10, 20, 30, 40, 50])
# print("NumPy array:")
# print(np_array)
# new_series = pd.Series(np_array)
# print("Converted Pandas series:")
# print(new_series)


####4 Write a Pandas program to convert the first column of a DataFrame as a Series


# import pandas as pd
# d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
# df = pd.DataFrame(data=d)
# print("Original DataFrame")
# print(df)
# s1 = df.ix[:,0]
# print("\n1st column as a Series:")
# print(s1)
# print(type(s1))


#####5 Write a Pandas program to sort a given Series

# import pandas as pd
# # s = pd.Series(['100', '200', 'python', '300.12', '400'])
# # print("Original Data Series:")
# # print(s)
# # new_s = pd.Series(s).sort_values()
# # print(new_s)

####6
##Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# import pandas as pd
# import numpy as np
# exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#         'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#         'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# df = pd.DataFrame(exam_data , index=labels)
# print("Rows where score between 15 and 20 (inclusive):")
# print(df[df['score'].between(15, 20)])


###7
# Write a Pandas program to calculate the sum of the examination attempts by the students.
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

# import pandas as pd
# import numpy as np
# exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#         'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#         'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data , index=labels)
# print("\nSum of the examination attempts by the students:")
# print(df['attempts'].sum()) 