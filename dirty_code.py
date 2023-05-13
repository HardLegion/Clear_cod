import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
company_names = ['Company A', 'Company B', 'Company C', 'Company D']
values = np.array([[30, 45, 22, 18],
                   [15, 30, 35, 10],
                   [20, 25, 15, 30],
                   [10, 40, 20, 30]])

# Set the style (optional)
plt.style.use('ggplot')

# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Create an index array for the x-axis
index = np.arange(len(categories))

# Define the width of each bar
bar_width = 0.15

# Create the bars for each company and category
for i in range(len(company_names)):
    plt.barh(index + i * bar_width, values[i], bar_width, label=company_names[i])

# Set the x-axis ticks and labels
plt.yticks(index + (len(company_names) - 1) * bar_width / 2, categories)

# Set the y-axis label
plt.ylabel('Categories')

# Set the x-axis label
plt.xlabel('Values')

# Set the plot title
plt.title('Grouped Horizontal Bar Chart')

# Add a legend
plt.legend()

# Save the chart to a file
plt.savefig('grouped_bar_chart.png')

# Display the chart
plt.show()
