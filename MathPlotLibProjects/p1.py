import matplotlib.pyplot as plot

x = range(50)
y = [i * 3 for i in x]

plot.plot(x, y)
plot.xlabel('X-Axis')
plot.ylabel('Y-Axis')
plot.title('Line Demo')

plot.show()
