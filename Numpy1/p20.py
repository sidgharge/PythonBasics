import math

rows = int(input("Enter number of rows: "))

# for row in range(rows):
#     print(' ' * (rows - row - 1), end='')
#
#     num = int(math.pow(11, row))
#
#     string = ' '.join(str(num))
#     print(string)

la = {}
for row in range(rows):
    temp = {0: 1, row: 1}

    for x in range(len(la) - 1):
        temp[x+1] = la[x] + la[x+1]

    la = temp
    print(' ' * (rows - row - 1), end='')

    if rows == 0:
        print(1)
    else:
        string = ' '.join(str(x) for x in la.values())
        print(string)
