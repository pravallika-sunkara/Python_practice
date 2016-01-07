'''
Your GOAL is to design a program that displays the number of days in each month. The program's output should be similar to this:
January has 31 days.
February has 28 days.
March has 31 days.
April has 30 days.
May has 31 days.
June has 30 days.
July has 31 days.
August has 31 days.
September has 30 days.
October has 31 days.
November has 30 days.
December has 31 days.
'''

def Main():
  month=['January','Feburary','March','April','May','June','July','August','September','October','November','December']
  days=[31,28,31,30,31,30,31,31,30,31,30,31]
  for i in range(0,12):
	  print month[i],'has',days[i],"days"

if __name__=='__main__':
  Main()
  
