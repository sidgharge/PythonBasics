class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name


user = User('Sid', 'Sid')

user_dict = user.__dict__

print(user_dict)

print(not bool(user_dict))
