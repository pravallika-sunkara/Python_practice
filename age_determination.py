'''
Sometimes a site might not be appropriate for people of a certain age. For times like these, we'll need a program that verifies the user's age, to ensure that they can view the site.
GOAL
Create a program that makes sure that the user is of an age of your choice (18 being the default).
SUB GOALS
Have the user input their birthday, and use that to determine if they are old enough
If the user is not of an appropriate age, suggest a different website/websites that would be appropriate for them
'''

import datetime

def Main():
  user_age=raw_input("Enter your date of birth (MM/DD/YYYY):  ")
  t=user_age.split("/")
  diff=2016-int(t[2])
  if diff < 18:
    print "You are underage."
  else:
    print "Enjoy the services provided by this website"
    

if __name__=='__main__':
  Main()
