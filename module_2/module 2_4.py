numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(1,len(numbers)):
    for n in range (2,numbers[i]-1):
        if numbers[i]%n != 0:
            is_prime = True
        else:
            is_prime = False
        if not is_prime:
            break
    if is_prime:
        primes.append(numbers[i])
    else:
         not_primes.append(numbers[i])
print('Primes:',primes)
print('Not primes:',not_primes)