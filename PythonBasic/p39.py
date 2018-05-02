
p = int(input("Enter amount: "))
r = float(input("Enter rate: ")) / 100
n = int(input("Enter years: "))

amt = p * ((1 + r) ** n)

print(amt)
