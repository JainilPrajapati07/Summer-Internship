n1 = int(input('Enter a number 1 : '))
n2 = int(input('Enter a number 2 : '))
n3 = int(input('Enter a number 3 : '))

if n1 > n2:
    if n1 > n3:
        print(n1,'is greatest number')
    else:
        print(n3,'is greatest number')
else:
    if n2 > n3:
        print(n2,'is greatest number')
    else:
        print(n3,'is greatest number')