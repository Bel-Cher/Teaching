#!/usr/bin/env python3

# Newton's Method

#import math
import sympy as sym

def get_func():
    print('\n')
    input_expr = input('Input a function in x, using the math library: \nf(x) = ')
    return input_expr

def func_eval(expr, x):
    
    print('f({}) = '.format(x) + str(eval(expr)))

def main():
    func = get_func()
    x = float(input('Enter a value: '))
    print('f({}) = '.format(x) + str(eval(func)))

if __name__ == '__main__':
    main()
