import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

# read data into a pandas dataframe and transpose
data = pandas.read_csv('gapminder_gdp_oceania.csv', index_col = 'country').T

# create a plot the transposed data
ax = data.plot()

# display the plot
plt.show()
