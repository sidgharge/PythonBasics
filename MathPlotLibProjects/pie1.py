import matplotlib.pyplot as plt

languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'

popularity = [22.2, 17.6, 8.8, 8, 7.7, 25.7]

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

explode = (0.1, 0, 0, 0, 0, 0.1)

plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', startangle=180, explode=explode,
        counterclock=False)
plt.axis('equal')
plt.title(s='Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago', bbox={'facecolor':'0.8', 'pad':5})
plt.show()
