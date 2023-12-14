name = input('What is your full name? ').lower().strip()

print('it has:',name.count('a'),'a(s)')
print('first a appears at:',name.index('a')+1)
print('last a appears at:',name.rindex('a')+1)


"""
txt = "Hello World"[::-1]
print(txt)
"""