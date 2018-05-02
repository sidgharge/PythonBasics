
def eq(num1, num2):
    if (num1 == num2) or ((num1 + num2) == 5) or (abs(num1 - num2) == 5):
        return True
    else:
        return False


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print(eq(num1, num2))
