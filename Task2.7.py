###Task 2.7


####1

# Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
#
#
# import matplotlib.pyplot as plt
# X = range(1, 50)
# Y = [value * 3 for value in X]
# print("Values of X:")
# print(*range(1,50))
# print("Values of Y (thrice of X):")
# print(Y)
# plt.plot(X, Y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Draw a line.')
# plt.show()


#####2

# Write a Python program to draw line charts of the financial data of Alphabet Inc.
# between October 3, 2016 to October 7, 2016
# Data
# 10-03-16,774.25,776.065002,769.5,772.559998
# 10-04-16,776.030029,778.710022,772.890015,776.429993
# 10-05-16,779.309998,782.070007,775.650024,776.469971
# 10-06-16,779,780.47998,775.539978,776.859985
# 10-07-16,779.659973,779.659973,770.75,775.080017

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
# df.plot()
# plt.show()

###3

# Write a Python program to display the grid and draw line charts of the closing value
# of Alphabet Inc. between October 3, 2016 to October 7, 2016.
# Customized the grid lines with linestyle -, width .5. and color blue.
# Data
# 03-10-16,772.559998
# 04-10-16,776.429993
# 05-10-16,776.469971
# 06-10-16,776.859985
# 07-10-16,775.080017

# import datetime as DT
# from matplotlib import pyplot as plt
# from matplotlib.dates import date2num
#
# data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
#         (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
#         (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
#         (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
#         (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]
#
# x = [date2num(date) for (date, value) in data]
# y = [value for (date, value) in data]
#
# fig = plt.figure()
#
# graph = fig.add_subplot(111)
# graph.plot(x,y,'r-o')
# graph.set_xticks(x)
# graph.set_xticklabels(
#         [date.strftime("%Y-%m-%d") for (date, value) in data]
#         )
# plt.xlabel('Date')
# plt.ylabel('Closing Value')
# plt.title('Closing stock value of Alphabet Inc.')
# plt.grid(linestyle="-", linewidth='0.5', color='blue')
# plt.show()

###4

# Write a Python programming to display a bar chart of the popularity of programming Languages
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# import matplotlib.pyplot as plt
# x = ['Java', 'Python', 'PHP', "JavaScript", 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# x_pos = [i for i, _ in enumerate(x)]
#
# plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')
#
# plt.xlabel("Languages")
# plt.ylabel('Popularity')
# plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
# plt.xticks(x_pos, x)
# plt.minorticks_on()
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()

###5

# Write a Python programming to create a pie chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7


# import matplotlib.pyplot as plt
# # # languages = 'Java', 'Python', 'PHP', "JavaScript", 'C#', 'C++'
# # # popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# # # colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# # # explode = (0.1, 0, 0, 0,0,0)
# # # plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
# # # autopct='%1.1f%%', shadow=True, startangle=140)
# # #
# # # plt.axis("equal")
# # #
# # # plt.show()

###6

# Write a Python program to draw a scatter graph taking
# a random distribution in X and Y and plotted against each other.

# import matplotlib.pyplot as plt
# from pylab import randn
# X = randn(200)
# Y = randn(200)
# plt.scatter(X,Y, color="r")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()