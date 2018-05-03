import os

dir = '/home/bridgeit2017/Sid'

for f in (os.listdir(dir)):
    if os.path.isfile(dir + '/' + f):
        print(f)
