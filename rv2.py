# Function review
def make_sandwich(*ingredients):
   """  doc string to document the function   """
   print(f'The sandwich is made of... ')
   for ingredient in ingredients:
      print(f'-{ingredient}')

make_sandwich('White Bread','Cheese','Ham')
def is_even(num):
   """ check whether the number passed in is even """
   if num % 2 == 0:
      return True
   return False
   # return num % 2 == 0
num = 11
if is_even(num):
   print(f'{num} is even')
else:
   print(f'{num} is odd')

# check for prime number
def is_prime(num):
   """ check for num is prime """
   if num < 2:
      return False
   for i in range(2, num // 2 +1):
      if num % i == 0:
           return False    
   return True 
    
num1=111
if is_prime(num1):
   print(f'{num1} is a prime number.')
else:
   print(f'{num1} is not a prime number.')

# check for palindrome
def is_palindrome(word):
   """ check whether the word is palindrome  """
   '''
   end = len(word) // 2
   for i in range(end):
      if word[i] != word[-i-1]:
           return False
   return True
    '''
   return word == word [::-1]

word ='civic'
if is_palindrome(word):
   print(f'{word} is palindrome')
else:
   print(f'{word} is not palindrome')
#list
import random
num_list = []
for i in range(10):
   num_list.append(random.randint(1,100))
print('Using loop:',num_list)
#list comprehension
num_list1 = [random.randint(1,100) for _ in range(10)]
print('Using  list comprehension:',num_list1)
num_list.append([1,2,3])
print('Adding using append:',num_list)
num_list.extend([1,2,3])
print('Adding using extend:',num_list1)
list1 = num_list
print(id(num_list),id(list1))
list2 = [num for num in num_list]
print(id(num_list),id(list2))  
