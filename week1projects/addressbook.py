from c import AddressBook

msg = '''1: Add a address
2: Firstname count
9: Quit
'''

try:
    address_book = AddressBook.read()
except FileNotFoundError:
    address_book = []

while True:
    choice = int(input(msg))
    if choice == 1:
        address = AddressBook.create_address()
        print(address)
        address_book.append(address)
        AddressBook.save(address_book)
    elif choice == 2:
        print(AddressBook.fname_count(input("Enter firstname: ")))
    else:
        break

