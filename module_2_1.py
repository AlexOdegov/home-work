first = input('Введите три целых числа:')
second = input('Введите три целых числа:')
third = input('Введите три целых числа:')
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
