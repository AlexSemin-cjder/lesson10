first = int(input('Ввидите число:'))
second = int(input('Ввидите число:'))
third = int(input('Ввидите число:'))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(1)

