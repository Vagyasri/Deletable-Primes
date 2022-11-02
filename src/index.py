#/usr/bin/env python3

import math

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

def list_of_list(prime_list):
    if not prime_list: return []

    list_of_list = []
    for i in range(len(prime_list)):
        new_list = get_prime_list((prime_list[i]))
        if not new_list: continue
        else: list_of_list.append(new_list)
    return list_of_list
