
string = input("Enter string: ")

if not string.startswith('Is'):
    string = 'Is' + string
print(string)
