import matplotlib.pyplot as plt

x = [2, 4, 8, 10]
y = [2, 8, 8, 2]

choice = 4

# Plot Line
if choice == 1:
    plt.plot(x, y)
    plt.show()
# Bar Graph (Compare Values)
elif choice == 2:
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Graph")
    plt.bar(x, y, label="Graph", color="r", width=0.5)
    plt.show()
# Histogram (Compare Frequency)
elif choice == 3:
    h = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5]

    plt.hist(h)
    plt.show()
# Scatter Plot (Points)
else:
    plt.scatter(x, y)
    plt.show()
