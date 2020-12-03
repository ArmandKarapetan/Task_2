###Task2.9

##1
#
# Write a Pandas program to create
# a) Datetime object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# f) Time from a datetime.
# g) Current local time.
#
#
# import datetime
#
# from datetime import datetime
# print("Datetime object for Jan 11 2012:")
# print(datetime(2012, 1, 11))
# print("\nSpecific date and time of 9:20 pm")
# print(datetime(2011, 1, 11, 21, 20))
# print("\nLocal date and time:")
# print(datetime.now())
# print("\nA date without time: ")
# print(datetime.date(datetime(2012, 5, 22)))
# print("\nCurrent date:")
# print(datetime.now().date())
# print("\nTime from a datetime:")
# print(datetime.time(datetime(2012, 12, 15, 18, 12)))
# print("\nCurrent local time:")
# print(datetime.now().time())

##2

# Write a Pandas program to print the day after and before a
# specified date. Also print the days between two given dates.
#
#
# import pandas as pd
# import datetime
# from datetime import datetime, date
# today = datetime(2012, 10, 30)
# print("Current date:", today)
# tomorrow = today + pd.Timedelta(days=1)
# print("Tomorrow:", tomorrow)
# yesterday = today - pd.Timedelta(days=1)
# print("Yesterday:", yesterday)
# date1 = datetime(2016, 8, 2)
# date2 = datetime(2016, 7, 19)
# print("\nDifference between two dates: ",(date1 - date2))

###3

# Write a Pandas program to create a date from
# a given year, month, day and another date from a given string format.
#
# import datetime
# from dateutil import parser
# from datetime import datetime
# date1 = datetime(year=2020, month=12, day=25)
# print("Date from a given year, month, day:")
# print(date1)
# date2 = parser.parse("1st of January, 2021")
# print("\nDate from a given string formats:")
# print(date2)

##4

# Write a Pandas program to create
# a date range using a startpoint date and a number of periods.
#
# import pandas as pd
# date_range = pd.date_range('2020-01-01', periods=10)
# print("Date range of perods 10:")
# print(date_range)
# #5
# Write a Pandas program to create a time series using three months frequency.
#
#
#
#
#
#
#
#
#
#
#
#
#
