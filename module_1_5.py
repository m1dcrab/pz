immutable_var = 1, True, 3.1, 'gg'
print (immutable_var)
#immutable_var[1] = 2; TypeError: 'tuple' object does not support item assignment

mutable_list = [1,2,False,True,7]
print (mutable_list)
mutable_list[1] = True; mutable_list[3] = 'Galo'
print (mutable_list)