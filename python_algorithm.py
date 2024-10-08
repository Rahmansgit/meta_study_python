# Algorithm for a palindrome

str = 'racecar'

# breakdown problem into smaller pieces
# 1st Step: Check the first and last character is same or not using index.
# print(str[0])
# print(str[6])

# 2nd Step: need to check each characters

# [0] == [6]
# [1] == [5]
# [2] == [4]

# 3rd step:

def isPalindrome(str):
  startIndex = 0
  endIndex = len(str) - 1 # remember last index is always -1 as index starts from '0'

  for i in str: # creating a for loop
    if str[startIndex] != str[endIndex]: # checking the letters through index
      return False # if condition mets it is not a palindrome
  return True # if condition not met it is a palindrome

print(isPalindrome('racecar'))