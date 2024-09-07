import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

# Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create a plot
# plt.plot(x, y)


# plt.plot(x, y, label="Line")
# plt.legend()


# # Show the plot
# sizes = [15, 30, 45, 10]
# labels = ['A', 'B', 'C', 'D']

# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title("Pie Chart")
# plt.show()



# data = np.random.randn(1000)  # Generate random data
# plt.hist(data, bins=10, color='red')
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)


data = [['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles'], ['Charlie', 35, 'Chicago']]
columns = ['Name', 'Age', 'City']

df = pd.DataFrame(data, columns=columns)
print(df)

df['Age'].plot(kind='hist')
plt.show()

