'''Problem: Write a program for sorting elements of an array in descending order and find the largest number.'''

import random
def desc(A):
  temp=0
  for i in range(0,len(A)):
    for j in range(0,len(A)):
      if A[i]>A[j]:
        temp=A[i]
        A[i]=A[j]
        A[j]=temp
  print "Descending order of elements:", A
  
def max_element(A):
  print "Largest number in the array:",max(A)

if __name__=='__main__':
  N=int(raw_input("Enter the number of elements in the array:"))
  A=[]
  for i in range(0,N):
    p=random.randint(0,100)
    A.append(p)
  print "Original elements in the array:",A
  desc(A)
  max_element(A)
