'''Write a method to decide if two strings are anagrams or not. '''
'''This code describes if the two strings entered by the user are the same when rearranged or not. '''


def find_angrams(num1,num2):
  test1=sorted(list(num1))
  test2=sorted(list(num2))
  if test1 == test2:
    print("These two strings are Anagrams of each other")
  else:
    print("These two strings are not Anagrams of each other")

num1 = raw_input("Enter the first string: ")
num2 = raw_input("Enter the second string: ")

find_angrams(num1,num2)
