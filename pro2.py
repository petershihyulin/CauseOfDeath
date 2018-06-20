import pandas as pd

df = pd.read_csv('TopCauseOfDeath.csv')
df2 = pd.read_csv('national_deaths.csv')

national = df2.groupby('Cause of death')[['Deaths']].sum()

national = national.sort_values(['Deaths'], ascending=False)

national = national[0:5]

national.to_csv('national.csv')

