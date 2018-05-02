
num1 = int(input("First num: "))
num2 = int(input("Last num: "))

multiplier = 1

while True:
    num = num1 * multiplier
    if num % num2 == 0:
        print("LCD: ", num)
        break
    multiplier += 1
