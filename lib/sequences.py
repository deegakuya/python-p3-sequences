#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    while len(fibonacci_list) < length:
        if len(fibonacci_list) == 0:
            fibonacci_list.append(0)
        elif len(fibonacci_list) == 1:
            fibonacci_list.append(1)
        else:
            next_value = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_value)
    print(fibonacci_list)
