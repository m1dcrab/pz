my_dict = {'u1name': 'Vova', 'u1date': 2002, 'u2name': 'Dima', 'u2date': 2007}
print ('словарь:',my_dict)
print ('ключ:',my_dict.get('u1name','ошибка'))
print ('ключа нет:',my_dict.get('wrong','ошибка'))
pop_ = my_dict.pop('u2name')
print ('значение удаленного ключа "u2name":',pop_)
print ('измененный словарь:',my_dict)

my_set = {3,0.00,0,True,'one',3,7,True,False,(1,2,4)}
print('множество:',my_set)
my_set.add(5+5)
my_set.add('test')
my_set.remove(False)
print('измененное множество:',my_set)
