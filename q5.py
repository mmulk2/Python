import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

# Load csv data
possum = pd.read_csv('yukon.csv')

g = sns.lmplot(y = "density", x = "cones", data = possum, ci = None)

plt.xlim(0, 6) #change the range of x axis

model_modified = stats.linregress(x = possum['cones'],
                                  y = possum['density'])

possum_modified2 = possum.copy()
# get length to loop from beginning to last row - 1 (which removes the outlier)
getLength = len(possum_modified2)
# modifies list by removing last row
possum_modified2 = possum_modified2[0:getLength - 1]

# Building a new model using the modified dataframe
possum_model_modified = stats.linregress(x = possum_modified2['cones'],
                                  y = possum_modified2['density'])

print(f"r^2: {possum_model_modified.rvalue ** 2}")
# print(f"slope: {possum_model_modified.slope}")


# print(possum_modified2.tail())


# print(f"r^2: {model_modified.rvalue ** 2}")

#plt.show()


