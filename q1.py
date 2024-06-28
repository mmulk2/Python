import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# Given probabilities
P_A = 0.35
P_B = 0.28
P_C = 0.50
P_A_and_B = 0.11
P_A_and_C = 0.15
P_B_and_C = 0.17
P_A_and_B_and_C = 0.07

# Calculate set sizes
size_A = round(P_A - P_A_and_B - P_A_and_C + P_A_and_B_and_C, 2)
size_B = round(P_B - P_A_and_B - P_B_and_C + P_A_and_B_and_C, 2)
size_C = round(P_C - P_A_and_C - P_B_and_C + P_A_and_B_and_C, 2)
size_A_and_B = round(P_A_and_B, 2)
size_A_and_C = round(P_A_and_C, 2)
size_B_and_C = round(P_B_and_C, 2)
size_A_and_B_and_C = round(P_A_and_B_and_C, 2)

# Plot Venn diagram
venn3(subsets=(size_A, size_B, size_A_and_B, size_C, size_A_and_C, size_B_and_C, size_A_and_B_and_C),
      set_labels=('A', 'B', 'C'), set_colors=("orange", "blue", "red"), alpha=0.7)

venn3_circles(subsets=(size_A, size_B, size_A_and_B, size_C, size_A_and_C, size_B_and_C, size_A_and_B_and_C),
               linestyle="-", linewidth=2)

plt.title("Venn diagram for A, B, C")
plt.show()

