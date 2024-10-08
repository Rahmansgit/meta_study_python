# set does't allow duplicate values:

set_a = {1, 2, 3 ,4 , 5, 5}

# in order to add the value in the set

set_a.add(6)

# to remove the value, its not index, directly need to remove value.
set_a.remove(2)

# another method to remove

set_a.discard(1)

print(set_a)

set_b = {1, 2, 4, 5, 8, 4, 7}

# to join two sets, without duplicate values

print(set_a.union(set_b))

# another method to join

print(set_a | set_b)

# intersection - will match both set_a and set_b

print(set_a.intersection(set_b))

#another method

print(set_a & set_b)

# difference, only elements in set_a not in set_b

print(set_a.difference(set_b))

#another method

print(set_a - set_b)

#symmetrical difference, provide elements not in both sets

print(set_a.symmetric_difference(set_b))

# another mothod

print(set_a ^ set_b)

# its a unordered list, cannot able to access through index