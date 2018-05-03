import os
import time

path = '/home/bridgeit2017/Sid/jwts.txt'

print(time.ctime(os.path.getctime(path)))
print(time.ctime(os.path.getmtime(path)))
