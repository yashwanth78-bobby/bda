pip install matplotlib pandas
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Plotting
plt.plot(x, y, marker='o', label='Line Plot')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# Plotting
plt.bar(categories, values, color='skyblue')
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
import matplotlib.pyplot as plt

# Sample data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Plotting
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Plotting
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
import matplotlib.pyplot as plt

# Sample data
labels = ['Python', 'Java', 'C++', 'Ruby']
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # Explode 1st slice

# Plotting
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart Example")
plt.show()
#df visualization with python
import pandas as pd

# Sample data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Sales': [200, 250, 300, 350, 400]}

df = pd.DataFrame(data)

# Line plot
df.plot(x='Year', y='Sales', kind='line', marker='o', title='Sales Over Years')
plt.show()

# Bar plot
df.plot(x='Year', y='Sales', kind='bar', title='Sales Over Years')
plt.show()



#seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Sample data
data = np.random.randn(100)
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
df = pd.DataFrame({'Category': np.random.choice(categories, 100), 'Value': data})

# Matplotlib Histogram
plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram")
plt.show()

# Seaborn Bar Plot
sns.barplot(x=categories, y=values, palette='viridis')
plt.title("Bar Plot")
plt.show()

# Seaborn Scatter Plot
sns.scatterplot(x=np.random.randn(50), y=np.random.randn(50), hue=np.random.choice(categories, 50), palette='deep')
plt.title("Scatter Plot")
plt.show()

# Seaborn Box Plot
sns.boxplot(x='Category', y='Value', data=df, palette='pastel')
plt.title("Box Plot")
plt.show()

