favorites = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisu", "Chocolate cake"]

# for loop starts with '0'
for item in favorites:
  print("I like the desert", item)


print()
# while loop, if not count assigned, will lead to infinte loop
count = 0

while count < len(favorites):
  print("I like this desert", favorites[count])
  count += 1