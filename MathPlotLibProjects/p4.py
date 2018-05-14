import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('p4_file.csv', index_col=0)
df.plot(x=df.index, y=df.columns)
plt.show()
