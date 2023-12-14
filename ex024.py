city = input('Type a city name: ')

print("Yes, there is Santo.") if "santo" in city.lower() else print("No, there is not Santo.")


"""
Another method.
"""
print(' ')

check = city.lower().find('santo')
print("Yes, there is Santo.") if check >= 0 else print("No, there is not Santo.")