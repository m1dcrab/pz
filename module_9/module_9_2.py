first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(f_str) for f_str in first_strings if len(f_str) >= 5]
second_result = [(f_str, s_str) for f_str in first_strings for s_str in second_strings if len(f_str) == len(s_str)]
third_result = {t_str:len(t_str) for t_str in first_strings + second_strings if len(t_str) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
