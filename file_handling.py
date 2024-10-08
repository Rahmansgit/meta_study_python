file = open('text.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

# another method is with open, it will automatically close

with open('text.txt', mode = 'r') as file:
  data = file.readline()
  print(data)