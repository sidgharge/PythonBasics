import os.path as p

file_name = input("Enter filename: ")

if p.isfile(file_name):
    print('File exists')
else:
    print('File does not exist')
