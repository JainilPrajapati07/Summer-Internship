n = int(input('Enter a number : '))

if n < 100:
    if n % 2 == 0:
        print('Number is even...')
    else:
        print('number is odd...')
else:
    print('Number is greater than 100 or equal to 100')