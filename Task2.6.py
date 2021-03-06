#####Task 2.6


###1
#Write a Pandas program to split the following dataframe into groups based on school code3


# import pandas as pd
# pd.set_option('display.max_rows', None)
# student_data = pd.DataFrame({
#     'school_code': ['s001','s002','s003','s001','s002','s004'],
#     'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#     'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#     'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#     'age': [12, 12, 13, 13, 14, 12],
#     'height': [173, 192, 186, 167, 151, 159],
#     'weight': [35, 32, 33, 30, 31, 32],
#     "address": ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
#     index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#
# print("Original DataFrame:")
# print(student_data)
# print('\n Split the said data on school_code wise:')
# result = student_data.groupby(['school_code'])
# for name,group in result:
#     print("\nGroup:")
#     print(name)
#     print(group)
# print('\n Type of the object:')
# print(type(result))

###2

# Write a Pandas program to split the following given dataframe by school code and get mean, min,
# and max value of age for each school


# import pandas as pd
# pd.set_option('display.max_rows', None)
# student_data = pd.DataFrame({
#     'school_code': ['s001','s002','s003','s001','s002','s004'],
#     'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#     'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#     'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#     "age": [12, 12, 13, 13, 14, 12],
#     'height': [173, 192, 186, 167, 151, 159],
#     'weiglt': [35, 32, 33, 30, 31, 32],
#     'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
#     index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#
# print("Original DataFrame:")
# print(student_data)
# print('\nMean, min, and max value of age for each value of the school:')
# grouped_single = student_data.groupby('school_code').agg({'age': ['mean', 'min', 'max']})
# print(grouped_single)

###3

###Write a Pandas program to split the
# following given dataframe into groups based on school code and class

# import pandas as pd
# pd.set_option('display.max_rows', None)
# student_data = pd.DataFrame({
#     'school_code': ['s001','s002','s003','s001','s002','s004'],
#     'classs': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#     'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#     'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#     'age': [12, 12, 13, 13, 14, 12],
#     "height": [173, 192, 186, 167, 151, 159],
#     'weight': [35, 32, 33, 30, 31, 32],
#     'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
#     index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
# print("Original DataFrame:")
# print(student_data)
# print('\nSplit the said data on school_code, class wise:')
# result = student_data.groupby(['school_code', 'class'])
# for name,group in result:
#     print("\nGroup:")
#     print(name)
#     print(group)
#

###4

# Write a Pandas program to split the following given dataframe into groups based
# on school code and cast grouping as a list

# import pandas as pd
# pd.set_option('display.max_rows', None)
# student_data = pd.DataFrame({
#     'school_code': ['s001','s002','s003','s001','s002','s004'],
#     'classs': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#     'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#     'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#     'age': [12, 12, 13, 13, 14, 12],
#     "height": [173, 192, 186, 167, 151, 159],
#     'weight': [35, 32, 33, 30, 31, 32],
#     'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
#     index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
# print("Original DataFrame:")
# print(student_data)
# print('\nCast grouping as a list:')
# result = student_data.groupby(['school_code'])
# print(list(result))

####5

# Write a Pandas program to split a dataset, group by one column and get mean, min,
# and max values by group. Using the following dataset find the mean, min,
# and max values of purchase amount (purch_amt) group by customer id (customer_id)

# import pandas as pd
# pd.set_option('display.max_rows', None)
# orders_data = pd.DataFrame({
# 'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
# 'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
# 'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
# 'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
# 'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
# print("Original Orders DataFrame:")
# print(orders_data)
# result = orders_data.groupby('customer_id').agg({'purch_amt': ['mean', 'min', 'max']})
# print("\nMean, min, and max values of purchase amount (purch_amt) group by customer id  (customer_id).")
# print(result)






