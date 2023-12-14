from datetime import datetime
year = datetime.now().year

adults = 0
kids = 0

for i in range(0,7):
    birth = int(input('In which year were You born? '))
    if year-birth >= 18:
        adults+=1
    else:
        kids+=1

print('We have {} adults and {} kids.'.format(adults, kids))