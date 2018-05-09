import pickle


class Person:

    def __init__(self, name, dob, show_dob):
        self.name = name
        self.dob = dob
        self.show_dob = show_dob

    @classmethod
    def create_person(cls):
        name = input("Enter the name: ")
        dob = input("Enter the date of birth: ")
        show = input("Show dob? y or n")
        if show == 'y':
            show_dob = True
        else:
            show_dob = False
        return cls(name, dob, show_dob)

    @staticmethod
    def save(arr):
        with open('persons.dat', 'wb') as file:
            pickle.dump(arr, file)

    @staticmethod
    def read():
        with open('persons.dat', 'rb') as file:
            return pickle.load(file)

    def __str__(self):
        return 'name: {}, dob: {}, show_dob: {}'.format(self.name, self.dob, self.show_dob)

    def __repr__(self):
        return 'name: {}, dob: {}, show_dob: {}'.format(self.name, self.dob, self.show_dob)

