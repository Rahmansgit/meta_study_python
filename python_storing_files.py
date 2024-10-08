# To select the random pet name from the pet names list.

import random

f = open("petnames.txt", "r") # to open the file
f_content = f.read()  # to read the file
f_content_list = f_content.split("\n") # convert into array
f.close() # closing the file
print(random.choice(f_content_list))