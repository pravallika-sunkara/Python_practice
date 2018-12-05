'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

'''


from datetime import date
from datetime import time
from datetime import timezone
from datetime import datetime

def main():
    name = input ('Enter your name: ')
    age  = int(input('Enter your age: '))
    now  = datetime.now()

    currentyear = now.strftime('%Y')
    birthyear   = int(currentyear) - age 
    futureyear  = 100 + int(birthyear)
    print (name,' will be 100 years in the year ',futureyear)


if __name__ == '__main__':
    main()
