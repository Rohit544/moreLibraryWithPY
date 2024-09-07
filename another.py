import matplotlib.pyplot as plt
import numpy as np
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.plot(x, y)


plt.plot(x, y, label="Line")
plt.legend()


# Show the plot
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()



data = np.random.randn(1000)  # Generate random data
plt.hist(data, bins=10, color='red')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

