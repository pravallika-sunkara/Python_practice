'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
'''

def main():
    num  = int(input('Enter a number: '))
    if num%2 == 0:
        print ('The number given is an even number')
    else:
        print('The number given is an odd number')


if __name__ == '__main__':
    main()
