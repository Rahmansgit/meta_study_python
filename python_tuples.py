# tuples are deined by open and closed parenthesis

my_tuples = (1, 'strings', 4.55, True)

# accessing through index

print(my_tuples[1])
print(type(my_tuples))

# tuple look at the value only: example, it will give an output as index value '1'

print(my_tuples.count('strings'))

# iterate the loop

for x in my_tuples:
  print(x)

# the main difference between list and tuples is that tuples is immutable(we cannot able change the value)

# my_tuples[1] = 5

#TypeError: 'tuple' object does not support item assignment, as tuple cannot be reassigned, it is immutable   