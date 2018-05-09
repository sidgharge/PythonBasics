from a import Person

msg = '''1: Add a person
2: Show date of birth from name
3: Quit
'''
try:
    persons = Person.read()
except FileNotFoundError:
    persons = []

while True:
    choice = int(input(msg))
    if choice == 1:
        person = Person.create_person()
        persons.append(person)
        Person.save(persons)
    elif choice == 2:
        name = input("Enter name of the person: ")
        for p in persons:
            if p.name == name:
                if p.show_dob:
                    print(p.dob)
                else:
                    print("Secret")
    else:
        break

