'''''
# recursion demo
def func():
    x=10
    func()
from sys import getrecursionlimit
from sys import setrecursionlimit

def get_recursion_limit():
    print(f'Recursion limit:{getrecursionlimit()}')
get_recursion_limit()

def set_recursion_limit(num):
    setrecursionlimit(num)
    print(f'Recursion limit has been set to:{getrecursionlimit()}')

rec_limit =2000
set_recursion_limit(rec_limit)
################ count down example
# iterative way
def count_down(n):
    """ iterative count down """
    for i in range(n,-1,-1):
        print(f'Count from to:{i}')
print(f'\nIterative count down:')
count_down(5)
# recursive way
def count_down_re(n):
    """ recursive count down """
    # base case
    if n < 0:
        return
    print(f'count down to:{n}')
    count_down_re(n-1)
print(f'\nRecursive count down:')
count_down_re(5)
################## sum digits
def sum_digit(num):
    """ sum all digits of a number """
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total
print(f'\nIterative sum digit:')
num = 123456789
total = sum_digit(num)
print(f'Sum of all digits of {num}:{total}')
# recursive way
def sum_digit_re(num):
    """ recursive sum digit """
    # base case
    if num % 10 == num:
        return num
    return num % 10 + sum_digit_re(num // 10)
print(f'\nRecursive sum digit:')
print(f'Sum of all digits of {num}:{sum_digit_re(num)}')
################## factorial()
# Iterative way
def factorial(n):
    """ Interative factorial"""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(f'\nIterative factorial()')
result = factorial(5)
print(f'factorial(5) = {result}')
# Recursive way
def factorial_re(n):
    """ recursive factorial """
    # base case
    print(f'factorial() called with n= {n}')
    result = 1 if n <= 1 else n * factorial_re(n-1)
    print(f'factorial({n}) returns {result}')
    return result
print(f'\nRecursive factorial()')
n = 5
result = factorial_re(n)
print(f'n = {n}, factorial of {n} = {result}')
'''
###############################################
# Performance checking
from timeit import timeit
print(f'\nCheck for performance of factorial in differrent settings:')
setup_string =  """
print(f'from Recursive')
def factorial(n):
    return 1 if n<=1 else n* factorial(n-1)
"""
print(timeit('factorial(5)', setup=setup_string, number=10_000_000))

setup_string = """
print(f'from Iterative:')
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result = result +i
    return result 
"""
print(timeit('factorial(5)', setup=setup_string, number=10_000_000))
# using math module
setup_string = """
print(f'from Math Module built-in function:')
from math import factorial 
"""
print(timeit('factorial(5)', setup=setup_string, number=10_000_000))

#################################
# check palindrome 
def is_palindrome(s):
    """ check whether the string passed in is palindrome"""
    return s == s[::-1]
# recursive
def is_palindrome_re(s):
    """ check palindrome using recursive approach"""
    #base case
    if len(s) <=1 :
        return True
    return s[0] == s[-1] and is_palindrome_re(s[1:-1])
string = 'greetings'
print(f'Interative palindrome:{is_palindrome(string)}')
print(f'Recursive palindromre:{is_palindrome_re(string)}')
# check palindrome with helper function
def is_palindrome_helper(s, left, right):
    """ check palindrome using helper function"""
    if left >= right:
        return True 
    return s[left] == s[right] and is_palindrome_helper(s, left+1, right-1)
def is_palindrome_re1(s):
    """ palindrome function with helper"""
    return is_palindrome_helper(s,0,len(s)-1)
print(f'Palindrome with helper function:{is_palindrome_re1(string)}')


