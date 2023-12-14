nlist = []

for x in range(0,7):
    nlist.append(int(input('number please: ')))

sumif = 0
for i in nlist:
    if i % 2 == 0:
        sumif += i

print(sumif)