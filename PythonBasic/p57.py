import time

start_time = time.time()
sum = 0
for x in range(1000):
    sum += x
print(sum)
end_time = time.time()
print('Time taken: ', end_time - start_time)