speed = float(input('Let me know the speed you were going... '))

if speed > 80:
    bill = (speed-80)*7
    print('You got a ticket for surpassing the speed limit.')
    print('You must pay: ${} dollars'.format(bill))
else:
    print('Hmm... Have a nice day.')