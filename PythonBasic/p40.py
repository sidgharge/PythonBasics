import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dist = math.pow((x1 - x2) ** 2 + (y1 - y2) ** 2, 0.5)

print(dist)
