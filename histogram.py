import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://github.com/nytimes/covid-19-data/raw/master/us-counties.csv")

histo_plot = df['deaths'].hist(bins=200)
histo_plot.set_title('Deaths in a day by COVID-19')
histo_plot.set_xlabel('Deaths Number')
histo_plot.set_ylabel('Frequency')

plt.xlim([0, 1000])
plt.ylim([0, 500000])
plt.savefig('histogram.png')
