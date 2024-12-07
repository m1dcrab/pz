def is_prime(funct):
    def wrapper(*args):
        result_ = funct(*args)
        state = 'Простое'
        for i in range(2, result_ - 1):
            if result_ % i == 0:
                state = 'Составное'
                break
        print(state)
        return result_
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)
result = sum_three(2, 3, 6)

print(result)