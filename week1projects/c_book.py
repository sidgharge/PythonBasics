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
        self.fill_data(self)
        AddressBook.save()

    address_book = {'addresses': [], 'f_names': {}, 'l_names': {}, 'streets': {}}
    # address_book.addresses = []
    # address_book.f_names = {}
    # address_book.l_names = {}
    # address_book.streets = {}

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
            for address in address_book['addresses']:
                if address.mobile == mobile:
                    duplicate_mob = True
                    break
            if not duplicate_mob:
                break
        while True:
            email = input("Enter email: ")
            address_book = cls.address_book
            duplicate_email = False
            for address in address_book['addresses']:
                if address.email == email:
                    duplicate_email = True
                    break
            if not duplicate_email:
                break

        return cls(fname, lname, street_address, city, state, country, mobile, email)

    @classmethod
    def fill_data(cls, address):
        address_book = cls.address_book
        address_book['addresses'].append(address)

        fname_count = address_book['f_names'].get(address.fname.lower())
        if fname_count is None:
            fname_count = 0
        fname_count += 1
        address_book['f_names'][address.fname.lower()] = fname_count

        lname_count = address_book['l_names'].get(address.lname.lower())
        if lname_count is None:
            lname_count = 0
        lname_count += 1
        address_book['l_names'][address.lname.lower()] = lname_count

        street_count = address_book['streets'].get(address.street_address.lower())
        if street_count is None:
            street_count = 0
        street_count += 1
        address_book['streets'][address.street_address.lower()] = street_count

    @classmethod
    def save(cls):
        with open('addressbook2.dat', 'wb') as file:
            pickle.dump(cls.address_book, file)

    @classmethod
    def read(cls):
        with open('addressbook2.dat', 'rb') as file:
            cls.address_book = pickle.load(file)
            print(cls.address_book)
            return cls.address_book

    @classmethod
    def fname_count(cls, fname):
        return cls.address_book['f_names'].get(fname.lower())

    @classmethod
    def lname_count(cls, lname):
        return cls.address_book['l_names'].get(lname.lower())

    @classmethod
    def street_count(cls, street_name):
        return cls.address_book['streets'].get(street_name.lower())

    @classmethod
    def count(cls, field_name, field_val):
        return cls.address_book[field_name].get(field_val.lower())

    def __repr__(self):
        return 'fname: {}, lname: {}, street_address: {}, city: {}, state: {}, country: {}, mobile: {}, email: {}' \
            .format(self.fname, self.lname, self.street_address, self.city, self.state, self.country, self.mobile,
                    self.email)

