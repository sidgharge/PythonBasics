import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pie4.csv')

countries = df['country']
medals = df['gold_medal']
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)

plt.pie(medals, labels=countries, colors=colors, explode=explode, autopct='%1.2f%%', counterclock=False, startangle=180)
plt.axis('equal')
plt.title('Gold medal achievements of five most successful\ncountries in 2016 Summer Olympics')

plt.show()
