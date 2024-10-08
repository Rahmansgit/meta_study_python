#To create a file:
# 
with open('newfile.txt', 'w') as file:
  file.write("This is a new file created")


# in order to add another line inside newfile.

with open('newfile.txt', 'w') as file:
  file.writelines(["This is a new file created.","This is another line to be added."])

# content to be break on a new line backslash and n

with open('newfile.txt', 'w') as file:
  file.writelines(["This is a new file created.","\nThis is another line to be added."])

# To add new lines, change the mode append 'a'.

  with open('newfile.txt', 'a') as file:
    file.writelines(["\nThis is a new file created.","\nThis is another line to be added."])


# if you dont know exact path, always use try and exception.

try:
  with open('newfile.txt', 'a') as file:
    file.writelines(["\nThis is a new file created.","\nThis is another line to be added."])
except FileNotFoundError as e:
  print("ERROR", e)