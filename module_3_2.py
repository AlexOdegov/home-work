def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

value_list = ['слово', 23, False]
value_dict = {'a' : 23, 'b' : 34, 'c' : 32}
print_params(*value_dict)
print_params(**value_dict)

values_list_2 = ['дело', 33]
print_params(*values_list_2, 42)
