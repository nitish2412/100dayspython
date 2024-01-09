import csv
import pandas
'''
fp = open("weather_data.csv", "r")
data = fp.readlines()
print(data)
fp.close()
'''
'''
with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
'''
'''
data = pandas.read_csv("weather_data.csv")
print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
n = len(temp_list)

avg_temp = sum(temp_list)/n
print(avg_temp)
print(data["temp"].mean())
print(data["temp"].max())

# Get data columns
print(data["condition"])
print(data.condition)


# Get data a row

print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp[0]

monday_temp_f = monday_temp*9/5 + 32
print(monday_temp_f)

# Create a data frame from scratch
data_dict = {
    "students": ["abnmd", "dsjks", "jdsks"],
    "score": [34, 76, 98]
}
data = pandas.DataFrame(data_dict)
print(data)
# data.to_csv("new_data.csv")
'''

data = pandas.read_csv("squirrel_data.csv")
# print(data.columns)
gray_squirrel_color_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_color_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_color_count)
print(red_squirrel_color_count)
print(black_squirrel_color_count)

data_dict ={
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_color_count, red_squirrel_color_count, black_squirrel_color_count]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")




