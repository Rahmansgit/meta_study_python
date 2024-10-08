def divided_by(a,b):
  return a/b
try:
  ans = divided_by(40,0)
except ZeroDivisionError as e:
  print("Something went wrong!",e)
  print(e.__class__) # to find out the expected errors

  # in order to do more precise way:
  print(e,"we cannot divided by zero")

# add another exception

except Exception as e:
  print("something went wrong")