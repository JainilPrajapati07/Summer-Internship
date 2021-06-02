n1 = int(input('Enter a number 1 : '))
n2 = int(input('Enter a number 2 : '))

if n1 == n2:
    print('Both numbers are same...')
else:
    if n1 < n2:
        print(n2,' is a greatest number...')
    else:
        print(n1,' is a greatest number...')