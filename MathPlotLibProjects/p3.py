import matplotlib.pyplot as plot

with open('p3_file.txt') as file:
    data = file.read()

rows = data.split('\n')

x = [row.split(' ')[0] for row in rows]
y = [row.split(' ')[1] for row in rows]

plot.plot(x, y)
plot.xlabel('X-Axis')
plot.ylabel('Y-Axis')
plot.title('Demo Graph')
plot.show()
