import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('california_death.csv')

df['Deaths'] = df['Deaths'].astype('int')

df = df[['Ten-Year Age Groups', 'Cause of death', 'Deaths']]

a = df[df['Cause of death']=='Atherosclerotic heart disease']
b = df[df['Cause of death']=="Alzheimer's disease, unspecified"]
c = df[df['Cause of death']=='Bronchus or lung, unspecified - Malignant neoplasms']
d = df[df['Cause of death']=='Acute myocardial infarction, unspecified']
e = df[df['Cause of death']=='Chronic obstructive pulmonary disease, unspecified']

def group(s):
    s = s.groupby('Ten-Year Age Groups')[['Deaths']].sum()
    return s
a = group(a)
b = group(b)
c = group(c)
d = group(d)
e = group(e)

"""    
a = a.groupby('Ten-Year Age Groups')[['Deaths']].sum()
b = b.groupby('Ten-Year Age Groups')[['Deaths']].sum()
c = c.groupby('Ten-Year Age Groups')[['Deaths']].sum()
d = d.groupby('Ten-Year Age Groups')[['Deaths']].sum()
e = e.groupby('Ten-Year Age Groups')[['Deaths']].sum()
"""

print(a,b,c,d,e)

names = ('25-35', '35-44', '45-54', '55-64', '65-74 ', '75-84', '85+')
Cause = ['Atherosclerotic heart disease', "Alzheimer's disease, unspecified", 'Bronchus or lung, unspecified - Malignant neoplasms', 'Acute myocardial infarction, unspecified', 'Chronic obstructive pulmonary disease, unspecified']
x = range(len(names))
y1 = a['Deaths'].tolist()
y2 = b['Deaths'].tolist()
y3 = c['Deaths'].tolist()
y4 = d['Deaths'].tolist()
y5 = e['Deaths'].tolist()

y2.insert(0, 0)
y2.insert(1, 0)
y2.insert(2, 0)
y3.insert(0, 0)
y5.insert(0, 0)
y5.insert(1, 0)


plt.plot(x, y1, 'ro-',x , y2, 'bo-',x , y4, 'yo-',x , y3, 'co-',x , y4, 'go-',x , y5, 'o-')
plt.xticks(x, names, rotation=45)
plt.margins(0.08)
plt.subplots_adjust(bottom=0.15)
plt.legend(Cause, loc="best")

plt.show()

