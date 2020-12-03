###2.5


####1
# Write a Pandas program to display all the records of REGIONS file


# import pandas as pd
# # employees = pd.read_csv(r"EMPLOYEES.csv")
# # departments = pd.read_csv(r"DEPARTMENTS.csv")
# # job_history = pd.read_csv(r"JOB_HISTORY.csv")
# # jobs = pd.read_csv(r"JOBS.csv")
# # countries = pd.read_csv(r"COUNTRIES.csv")
# # regions = pd.read_csv(r"REGIONS.csv")
# # locations = pd.read_csv(r"LOCATIONS.csv")
# # print("All the records from regions file:")
# # print(regions)

###2

# Write a Pandas program to display all the location id from locations file.


# import pandas as pd
#
# employees = pd.read_csv(r"EMPLOYEES.csv")
# departments = pd.read_csv(r"DEPARTMENTS.csv")
# job_history = pd.read_csv(r"JOB_HISTORY.csv")
# jobs = pd.read_csv(r"JOBS.csv")
# countries = pd.read_csv(r"COUNTRIES.csv")
# regions = pd.read_csv(r"REGIONS.csv")
# locations = pd.read_csv(r"LOCATIONS.csv")
#
# result = locations[['location_id']]
#
# print("All the locations id from locations file:")
#
# print(result)

###3

# Write a Pandas program to extract first 7 records from employees file.

# import pandas as pd
#
# employees = pd.read_csv(r"EMPLOYEES.csv")
# departments = pd.read_csv(r"DEPARTMENTS.csv")
# job_history = pd.read_csv(r"JOB_HISTORY.csv")
# jobs = pd.read_csv(r"JOBS.csv")
# countries = pd.read_csv(r"COUNTRIES.csv")
# regions = pd.read_csv(r"REGIONS.csv")
# locations = pd.read_csv(r"LOCATIONS.csv")
#
# print("First 7 records from employees file:")
# print(employees.head(7))

###4

# Write a Pandas program to select distinct department id from employees file.
#
# import pandas as pd
#
# employees = pd.read_csv(r"EMPLOYEES.csv")
# departments = pd.read_csv(r"DEPARTMENTS.csv")
# job_history = pd.read_csv(r"JOB_HISTORY.csv")
# jobs = pd.read_csv(r"JOBS.csv")
# countries = pd.read_csv(r"COUNTRIES.csv")
# regions = pd.read_csv(r"REGIONS.csv")
# locations = pd.read_csv(r"LOCATIONS.csv")
#
# print("Distinct department_id:")
# print(employees.department_id.unique())

###5

# Write a Pandas program to display the first, last name,
# # salary and department number for those employees whose first name starts with the letter 'S'.
#
# # import pandas as pd
# #
# # employees = pd.read_csv(r"EMPLOYEES.csv")
# # departments = pd.read_csv(r"DEPARTMENTS.csv")
# # job_history = pd.read_csv(r"JOB_HISTORY.csv")
# # jobs = pd.read_csv(r"JOBS.csv")
# # countries = pd.read_csv(r"COUNTRIES.csv")
# # regions = pd.read_csv(r"REGIONS.csv")
# # locations = pd.read_csv(r"LOCATIONS.csv")
# # print("First name       Last name      Salary    Department ID")
# # result = employees[employees['first_name'].str[0]=='S']
# # for index, row in result.iterrows():
# #     print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])