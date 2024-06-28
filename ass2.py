import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import percentile

# Reads the Mortality.csv data. Had to make sure to encode in CP1252 as one of the character was not recognized in UTF-8
mortalityRate = pd.read_csv('Mortality.csv',encoding='cp1252', skipinitialspace=True, sep=',',header=0)
# Strips space characters from the columns. For example "Country " has a space.
mortalityRate.columns = mortalityRate.columns.str.strip()
# Setting up dictonary with key and values which are Country and Rate
df_data = {"Country" : mortalityRate["Country"], "Rate" : mortalityRate["Rate"]}
# Transform dictionary into dataframe (table)
df = pd.DataFrame(data = df_data)

# Prints the first 10 elements and last 10 elements for all the data
print("\n\n\nPrints First 10 elements \n")
print(df.iloc[:10,:])
print("\n\n\nPrints Last 10 elements\n")
print(df.iloc[-10:,:])

# Prints the first 10 elements and last 10 elements ordered by Mortality Rate
print("\n\n\nPrints First 10 elements by Mortality Rate\n")
print(df.iloc[:10,1])
print("\n\n\nPrints Last 10 elements by Mortality Rate\n")
print(df.iloc[-10:,1])

# Changes the window size when plotting the histogram
plt.figure(figsize=[10,8])

# Defines the intervals between 0 and 140 exclusive meaning [0-130]
bins=np.arange(0, 140, 10)

# Sets the bin for the histogram to plot based on the column Rate
plt.hist(df["Rate"], bins=bins)
plt.xticks(bins)

# Labelling the x,y axis and title
plt.ylabel("Frequency",fontsize=15)
plt.xlabel("Countries with Child Mortality Rate (per 1000)", fontsize=15)
plt.title("Histogram of Child Mortality Rate (per 1000)\'s Across Countries", fontsize=15)

# Showing the histogram on a new Window
plt.show()

# Calculating summary statistics for the child mortality rate across countries.
quartile = percentile(df["Rate"],[25,50,75])
IQR = 1.5 * quartile[1]
print("IQR of Q1 " + str(quartile[0]-IQR) + " IQR of Q3 " + str(quartile[2]+IQR))
print("\n\nCalculating 5 Number Summary as Distribution: \nDistribution is skewed to the right: \nCalculating: Percentile, Median, Minimum and Maximum")
print("\n Q1 is: " + str(quartile[0]) +  "\n Q3 is: " + str(quartile[2]) +  "\n" + " Median is: " + \
      str(quartile[1]))
print(" Minimum is: " + str(min(df["Rate"])))
print(" Maximum is: " + str(max(df["Rate"])))

