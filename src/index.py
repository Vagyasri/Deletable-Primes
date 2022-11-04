#/usr/bin/env python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_prime_list(num):
    if not is_prime(num): return False

    num = str(num)
    prime_list = []
    for i in range(len(num)):
        new_num = int(num[:i] + num[i+1:])
        if not is_prime(new_num):
            continue
        else: prime_list.append(new_num)
    return prime_list

def flatten_list(digit_list):
    if not digit_list: return []

    new_list = []
    for i in range(len(digit_list)):
        if type(digit_list[i]) == int:
            new_list.append(digit_list[i])
        else:
            new_list += flatten_list(digit_list[i])
    return new_list

def get_prime_digit_list(num):
    prime_list = get_prime_list(num)
    new_list = []
    if not prime_list: return []
    for i in range(len(prime_list)):
        if 1 < prime_list[i] < 10: new_list.append(prime_list[i])
        else: new_list.append(get_prime_digit_list(prime_list[i]))
    return flatten_list(new_list)

def get_count(num):
    return len(get_prime_digit_list(num))
