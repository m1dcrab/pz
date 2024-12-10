def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5, 5, 1)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [6, 'тоже строка', False]
values_dict = {'a': True, 'b': 'и ещё строка', 'c': 0}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['fir', 'sec']
print_params(*values_list_2, 42)
