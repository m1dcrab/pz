from email.policy import strict

i = int(input('введите значение '))
result = []
for firstKeyNumber in range(1,i+1):
    for secondKeyNumber in range(1,i+1):
        if i % (firstKeyNumber+secondKeyNumber) == 0 and secondKeyNumber > firstKeyNumber:
            result.append(firstKeyNumber)
            result.append(secondKeyNumber)
print('код:', result)