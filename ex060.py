n = int(input('Give me one number! '))
s = 1

while n > 0:
    n += -1
    s += s*n
print(s)
