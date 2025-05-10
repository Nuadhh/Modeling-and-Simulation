import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Oakleaf_v2.csv')


plt.figure(figsize=(8, 6))
plt.hist(df['OakLeaves'], bins=15, color='green', edgecolor='black', alpha=0.7)

plt.xlabel('Oak Leaves (units)')
plt.ylabel('Frequency')
plt.title('Distribution of Oak Leaves on a Composter (Minecraft)')
plt.grid(axis='y', linestyle='--', alpha=0.5)


plt.show()