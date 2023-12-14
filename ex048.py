sumif = 0

for x in range(0,501):
    if x % 2 == 1 and x % 3 == 0:
        sumif += x

print(sumif)