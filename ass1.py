import pandas as pd
import matplotlib.pyplot as plt

# loading relationship data and percent data onto a list
df = pd.DataFrame({'Relationship': ['Sibling', 'Child', 'Parent', 'Spouse', 'Other relative', 'Not related'],
                   'percent': [0.3, 0.19, 0.13, 0.11, 0.08, 0.19]})
# sets the index to be relationship column
df.set_index('Relationship', inplace=True)
# adding colours to a list to apply colours to pie Chart based on the order given in assignment [Red - sibling, Light Blue - Child, Green - Parent, Yellow - Spouse, Brown - ..., Gray - ....]
colors = ['#FF0000','#ADD8E6','#008000','#FFFF00','#964B00','#808080']
# adds title, percent and colors and customizes the pie chart  
plot = df.plot.pie(title="Pie Chart Of Organ Donor and Recipient Relationship",legend=False, colors=colors, autopct='%1.1f%%', figsize=(7, 7), subplots=True)
# prints the Pie Chart on a Window
plt.show()