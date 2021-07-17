import pandas

# DataFrame ----> Table
# Series -------> Column

data = pandas.read_csv("weather_data.csv")
# print(data)

# Dictionary
data_dict = data.to_dict()
# print(data_dict)

# Data in Series / Column
temp = data["temp"]
# print(temp)

# Series to List with key
temp_list = data.temp.to_list()
# print(temp_list)

# Computational functions
max_temp = temp.max()
# print(max_temp)

# Filter columns
even_temp = data[data.temp % 2 == 0]
# print(even_temp)

# Create DataFrame
new_data_dict = {
    "student": ["John", "Jane", "Tommy"],
    "marks": [85, 77, 80],
}

new_data = pandas.DataFrame(new_data_dict)
print(new_data)

# Create CSV
new_data.to_csv("new_data.csv")
