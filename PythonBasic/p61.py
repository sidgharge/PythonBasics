# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

dist = int(input("Enter distance: "))

print("Feet to inches: ", dist * 12)
print("Feet to yards: ", dist / 3)
print("Feet to miles: ", dist / 5280)
