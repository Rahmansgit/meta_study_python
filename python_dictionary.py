my_d = {1: 'Test', 'Name': 'Jim' }

print(type(my_d))

print(my_d[1]) # its not index, accessing using key

# adding elements into dictionary

my_d[2] = 'Test 2'

print(my_d)

# update the key:

my_d[1] = 'Not a test'
print(my_d)

# if we put a duplicate key, it won't allow it, below the latest one is "not a test", so output will be lastest. 

my_d1 = {1: 'Test', 2: 'Paper', 1: "Not a test"}

print(my_d1)


# delete

del my_d1[1]

print(my_d1)


# iterate the dictionary

for x in my_d1:
  print(x) # this will print only the key


# in order to print key & values together:

for key,value in my_d1.items():
  print(str(key)+': '+value)