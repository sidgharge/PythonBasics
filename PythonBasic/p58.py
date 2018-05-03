
n = int(input("Enter n: "))

count = 0
sum = 0
while count < n:
    num = int(input("Enter a number: "))
    if num >= 0:
        sum += num
        count += 1

print(sum)
