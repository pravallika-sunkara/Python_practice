'''
The computer randomly generates a number. The user inputs a number, and 
the computer will tell you if you are too high, or too low. 
Then you will get to keep guessing until you guess the number.
'''



import random

def Main():
  orig=random.randint(0,100)
  number=int(input("Enter a number between 0 to 100: "))
  while True:
    diff=orig - number
    if diff<-1:
      print "this number is higher than the original"
    elif diff>1:
      print "this number is lower than the original"
    else:
      print "You have guessed the number right! Congratulations!"
      break
    number=int(input("Enter a number between 0 to 100: "))
  

if __name__=='__main__':
  Main()
