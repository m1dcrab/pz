calls = 0
def count_calls():
    global calls
    calls = calls+1

def string_info(string):
    count_calls()
    string = (len(string),string.upper(),string.lower())
    return string

def is_contains(string,list_to_search):
    count_calls()
    complete = False
    for i in range(0,len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            complete = True
            break
        else:
            complete = False
    return complete

print (string_info('Capybara'))
print (string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
