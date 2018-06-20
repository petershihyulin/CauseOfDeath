import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv('TopCauseOfDeath.csv')
df2 = pd.read_csv('national.csv')

df2.insert(1, 'National', 'National')
df.insert(1, 'National', 'California')

df = df.sort_values(['Cause of death'], ascending=False)
df2 = df2.sort_values(['Cause of death'], ascending=False)

# data to plot
 
National = df2['Deaths'].tolist()
California = df['Deaths'].tolist()

percentage = [1,2,3,4,5] 
i = 0

for i in range(0, len(National)): 
    percentage[i] ="%.2f" % round(California[i]/National[i]*100,2)
    i+=1

percentage = tuple(percentage)

listCause = df2['Cause of death'].tolist()
Cause = tuple(listCause)

print(listCause)

y_pos = np.arange(len(Cause))
colors = ['#624ea7', 'g', 'yellow', 'r', 'b'] 

plt.bar(y_pos, percentage, align='center', alpha=0.5, color = colors)
#plt.xticks(y_pos)
plt.ylabel('Percentage')
plt.title('Percentage of California and National')
purple_patch = mpatches.Patch(color='#624ea7', label='Chronic obstructive pulmonary disease, unspecified')
green_patch = mpatches.Patch(color='g', label='Bronchus or lung, unspecified - Malignant neoplasms')
yellow_patch = mpatches.Patch(color='yellow', label='Atherosclerotic heart disease')
k_patch = mpatches.Patch(color='r', label="Alzheimer's disease, unspecified")
marron_patch = mpatches.Patch(color='b', label='Acute myocardial infarction, unspecified')
plt.legend(handles=[purple_patch, green_patch, yellow_patch, k_patch, marron_patch], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
