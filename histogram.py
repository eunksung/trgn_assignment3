
import pandas as pd

df = pd.read_csv('us-counties.csv')

covid_california = df[(df.state == "California")]
covid_california.plot(x='date', y='cases', style='l')
