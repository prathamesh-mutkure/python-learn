import pandas

data = pandas.read_csv("squirral_data.csv")
color_data = data["Primary Fur Color"]

gray_data = color_data[color_data == "Gray"]
cinnamon_data = color_data[color_data == "Cinnamon"]
black_data = color_data[color_data == "Black"]

color_count_dict = {
    "Fur Color": ["gray", "red", "black", ],
    "Count": [len(gray_data), len(cinnamon_data), len(black_data), ],
}

squirrel_count_data_frame = pandas.DataFrame(color_count_dict)
squirrel_count_data_frame.to_csv("squirral_analysis.csv")

print(squirrel_count_data_frame)
