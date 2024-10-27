data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
data_structure_sum = []
def calculate_structure_sum(*args):
    for var_len in range(len(args)):
        if isinstance(args[var_len],list) or isinstance(args[var_len],tuple) or isinstance(args[var_len], set):
            calculate_structure_sum(*args[var_len])
        if isinstance(args[var_len],dict):
            for dict_key in args[var_len].keys():
                calculate_structure_sum(dict_key)
                calculate_structure_sum(args[var_len][dict_key])
        if isinstance(args[var_len],int):
            data_structure_sum.append(args[var_len])
        if isinstance(args[var_len],str):
            data_structure_sum.append(len(args[var_len]))
    return sum(data_structure_sum)
result = calculate_structure_sum(data_structure)
print(result)
