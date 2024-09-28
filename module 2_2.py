first = input('введите первое значение ')
second= input('введите второе значение ')
third= input('введите третье значение ')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)