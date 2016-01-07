def Main():
  address_book={}
  Prompt=raw_input("Do you want to enter a contact? (y/n): ")

  while Prompt=="y":
    name=raw_input("Enter name of the person: ")
    email=raw_input("Enter the email address: ")
    phone=raw_input("Enter the phone number: ")
    address_book[name]=email,phone
    address_book[name]=list(address_book[name])
    print ('\n')
    Prompt=raw_input("Do you want to enter a contact? (Y/N) ")
  f=open("test.txt","w")
  for address,value in address_book.iteritems():
    f.write(str(address)+":"'\n'+str(value)+'\n')
  f.close()

if __name__=='__main__':
  Main()
