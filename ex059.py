choice = 6
inserts = True

while choice != 5:
    if inserts:
        n1 = int(input('Type one number... '))
        n2 = int(input('Type another number... '))
        inserts = False
    
    print('+='*10)
    choice = int(input('What do You want to do? \n 1) Sum \n 2) Multiply \n 3) Highest \n 4) Insert new numbers \n 5) Exit \n'))
    if choice == 1:
        print('You choose the first operation! The sum between {} and {} is {}'.format(n1,n2,n1+n2))

    elif choice == 2:
        print('You choose the second operation! The multiplication between {} and {} is {}'.format(n1,n2,n1*n2))

    elif choice == 3:
        if n1 > n2:
            highest = n1
        elif n2 > n1:
            highest = n2
        else:
            highest = False
        
        if highest:
            print('You choose the third operation! The highest value between {} and {} is {}'.format(n1,n2,highest))
        else:
            print('{} and {} are the same! Try again with new numbers.'.format(n1,n2))

    elif choice == 4:
        print('You choose the fourth operation! So You wanna insert new numbers? Ok, go on.')
        inserts = True

    elif choice == 5:
        print('You decided to exit. Ok, see ya!')
    else:
        print('Sorry, there is no operation for this input. Please try again.')
