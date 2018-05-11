
def read_file(file_name):
    txt = open(file_name)
    print(txt.read())


# read_file('program1.txt')


def read_n_lines(file_name, n):
    from itertools import islice
    with open(file_name) as file:
        for line in islice(file, n):
            print(line)


# read_n_lines('program1.txt', 1)

def write_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)
        file.write('\nLast words')


# write_file('program3.txt', 'This file is for program 3')
# read_file('program3.txt')


def read_file_line_by_line(file_name):
    with open(file_name) as file:
        file_list = file.readlines()
        print(file_list)


read_file_line_by_line('program3.txt')
