import pickle


class AddressBook:

    def __init__(self, fname, lname, street_address, city, state, country, mobile, email):
        self.fname = fname
        self.lname = lname
        self.street_address = street_address
        self.city = city
        self.state = state
        self.country = country
        self.mobile = mobile
        self.email = email

    address_book = []

    @classmethod
    def create_address(cls):
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        street_address = input("Enter street address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        country = input("Enter country: ")
        while True:
            mobile = input("Enter mobile: ")
            address_book = cls.address_book
            duplicate_mob = False
            for address in address_book:
                if address.mobile == mobile:
                    duplicate_mob = True
                    break
            if not duplicate_mob:
                break
        while True:
            email = input("Enter email: ")
            address_book = cls.address_book
            duplicate_email = False
            for address in address_book:
                if address.email == email:
                    duplicate_email = True
                    break
            if not duplicate_email:
                break
        return cls(fname, lname, street_address, city, state, country, mobile, email)

    @staticmethod
    def save(arr):
        with open('addressbook.dat', 'wb') as file:
            pickle.dump(arr, file)

    @classmethod
    def read(cls):
        with open('addressbook.dat', 'rb') as file:
            cls.address_book = pickle.load(file)
            return cls.address_book

    @classmethod
    def fname_count(cls, fname):
        count = 0
        for address in cls.address_book:
            if address.fname == fname:
                count += 1
        return count

    @classmethod
    def lname_count(cls, lname):
        count = 0
        for address in cls.address_book:
            if address.lname == lname:
                count += 1
        return count

    @classmethod
    def street_count(cls, street_name):
        count = 0
        for address in cls.address_book:
            if address.street_address == street_name:
                count += 1
        return count

    def __repr__(self):
        return 'fname: {}, lname: {}, street_address: {}, city: {}, state: {}, country: {}, mobile: {}, email: {}'\
            .format(self.fname, self.lname, self.street_address, self.city, self.state, self.country, self.mobile,
                    self.email)

