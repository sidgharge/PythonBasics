
string = input("Enter the string: ")
copies = int(input("Enter number of copies: "))

if len(string) < 2:
    print(string * copies)
else:
    print(string[:2] * copies)
