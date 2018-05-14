import matplotlib.pyplot as plt

x1 = [10, 20, 30]
y1 = [20, 40, 10]

plt.plot(x1, y1, label="Line 1")

x2 = [10, 20, 30]
y2 = [40, 10, 30]

plt.plot(x2, y2, label="Line 2")

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.title('Demo')

plt.show()
