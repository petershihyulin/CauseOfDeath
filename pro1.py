import pandas as pd
import matplotlib.pyplot as plt

#Step 1: Data Cleaning
#Import csv file
df = pd.read_csv('california_death.csv')

#1. Substring 
df.State = df.State.str.slice(0, 10)

#2. Convert data type
df['Deaths'] = df['Deaths'].astype('int')

#3. Delete useless columns
del df['Notes']

#Step 2: Process data
#Sum the amount of Cause of death
a = df.groupby('Cause of death')[['Deaths']].sum()

#Desc the value
b = a.sort_values(['Deaths'], ascending=False)

#Find the top 5 Cause of death
b = b[0:5]

b.to_csv('TopCauseOfDeath.csv')

#Step 3: Pie Chart
#Conver the amount into list
sizes = b['Deaths'].tolist()
labels = 'Atherosclerotic heart disease', 'Alzheimer\'s disease', 'Bronchus or lung', 'Acute myocardial infarction', 'Chronic obstructive pulmonary disease'
colors = ['red', 'blue', 'green', 'yellow', 'orange']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()



