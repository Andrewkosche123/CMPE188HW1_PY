import pandas as pd
import matplotlib.pyplot as plt

# initializing data and importing it to dataframe
data = [197, 199, 234, 267, 269, 276, 281, 289, 299, 301, 339]
df = pd.DataFrame(data)

# creating plot and adding appropriate title names
plot = df.plot.box(title='Title')
plot.set(xlabel='x axis', ylabel='y axis')

# saving the plot to pdf
plt.savefig('Q1_Python_Box_plot.pdf')

