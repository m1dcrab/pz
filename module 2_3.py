my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = -1
while True:
    count = count + 1
    if my_list[count] > 0:
        print(my_list[count])
    elif my_list[count] == 0:
        continue
    else:
        break