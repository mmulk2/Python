import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('tanana.csv')['Date']

# Plot the histogram
# plt.hist(data, bins=20, edgecolor='black')
# plt.title('Histogram of Ice Breakup Dates on Tanana River')
# plt.xlabel('Days from April 14')
# plt.ylabel('Frequency')
# plt.show()


import scipy.stats as stats
import numpy as np

# Given values
# sample_mean = data.mean()  # Sample mean
# population_std_dev = 7  # Population standard deviation
# sample_size = len(data)  # Sample size

# # Critical value for a 99% confidence interval
# z_value = stats.norm.ppf(0.995)  # 0.5% in each tail for a two-tailed test

# # Calculate margin of error
# margin_of_error = z_value * (population_std_dev / np.sqrt(sample_size))

# # Calculate confidence interval
# confidence_interval_lower = sample_mean - margin_of_error
# confidence_interval_upper = sample_mean + margin_of_error

# # Round to the nearest integer
# confidence_interval_lower = round(confidence_interval_lower)
# confidence_interval_upper = round(confidence_interval_upper)

# print(f'99% Confidence Interval: [{confidence_interval_lower}, {confidence_interval_upper}]')

import numpy as np

# Observations from the sample
data = np.array([63.4, 65.0, 64.4, 63.3, 54.8, 64.5, 60.8, 49.1, 51.0])

# Number of bootstrap samples
num_bootstrap_samples = 1000

# Bootstrap resampling
bootstrap_means = np.zeros(num_bootstrap_samples)

for i in range(num_bootstrap_samples):
    bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
    bootstrap_means[i] = np.mean(bootstrap_sample)

# Calculate the 95% percentile-based bootstrap confidence interval
confidence_interval = np.percentile(bootstrap_means, [2.5, 97.5])

print(f"95% Bootstrap Confidence Interval for the Mean Percentage of Nitrogen: {confidence_interval}")

# Present atmospheric nitrogen level
present_nitrogen_level = 78.1

# Check if the confidence interval overlaps with the present atmospheric level
overlap_present_level = (confidence_interval[0] <= present_nitrogen_level <= confidence_interval[1])

if overlap_present_level:
    print("The confidence interval overlaps with the present atmospheric nitrogen level. "
          "There is no strong evidence of a significant difference.")
else:
    print("The confidence interval does not overlap with the present atmospheric nitrogen level. "
          "There is some evidence of a significant difference.")


