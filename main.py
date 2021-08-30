# with open("weather_data.csv") as file:
#    data = file.readlines()

# print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     n=0
#
#     for row in data:
#         print(row)
#         n += 1
#         if n > 1:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas
from statistics import mean

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average_temp = mean(temp_list)
print(f"Average temp = {average_temp}")
av_temp = data["temp"].mean()
print(f"Average temp = {av_temp}")

max_temp = data["temp"].max()
print(f"Max temp = {max_temp}")

print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])

#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")









