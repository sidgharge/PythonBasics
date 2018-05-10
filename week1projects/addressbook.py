from c import AddressBook

msg = '''1: Add a address
2: First name count
3: Last name count
4: Street name count
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
        print(AddressBook.fname_count(input("Enter first name: ")))
    elif choice == 3:
        print(AddressBook.lname_count(input("Enter last name: ")))
    elif choice == 4:
        print(AddressBook.street_count(input("Enter street name: ")))
    else:
        break

