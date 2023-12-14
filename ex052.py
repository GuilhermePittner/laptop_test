n = int(input('number please; '))

sumdiv = 0
for x in range(1, n+1):
    if n%x==0:
        sumdiv+=1
   
if sumdiv <= 2:
    print('{} é primo'.format(n))
else:
    print('{} não é e nunca será primo'.format(n))