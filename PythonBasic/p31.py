
num1 = int(input("First num: "))
num2 = int(input("Second num: "))

if num1 > num2:
    smallest_num = num2
else:
    smallest_num = num1

gcd = 1

for num in range(1, smallest_num+1):
    if (num1 % num == 0) and (num2 % num == 0):
        gcd = num

print("GCD: ", gcd)
