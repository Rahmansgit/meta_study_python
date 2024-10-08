import time

start_time = time.time()


#outer loop
for i in range(100):
  #inner loop
  for i in range(100):
    print('*',end = " ")
  print()


print(round((time.time() - start_time), 2))
 