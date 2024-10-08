# example: function with 2 arguements

def sum_of(a,b):
  return a+b
print(sum_of(4,5))

# if we pass three arguments, TypeError: sum_of() takes 2 positional arguments but 3 were given 

# print(sum_of(4,5,6))

# for this *args come into picture, example:

def sum1_of(*args):
  sum1 = 0
  for i in args:
    sum1 += i
  return sum1

#we can pass as many arguments as we needed, so helpful
print(sum1_of(50,10,10))