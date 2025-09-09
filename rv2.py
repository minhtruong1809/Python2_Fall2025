
'''''
# Function review
def make_sandwich(*ingredients):
    doc string to document the function   
   print(f'The sandwich is made of... ')
   for ingredient in ingredients:
      print(f'-{ingredient}')

make_sandwich('White Bread','Cheese','Ham')
def is_even(num):
   check whether the number passed in is even 
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
    check for num is prime 
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
    check whether the word is palindrome 

   end = len(word) // 2
   for i in range(end):
      if word[i] != word[-i-1]:
           return False
   return True
    
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
print(id(num_list),id(list2)) 
'''''

# two dimensional list 

two_D = []
# use list comprehension to create 2D
two_D = [[col for col in range(10)] for row in range(5) ]
print(two_D)
for row in range(len(two_D)):
    for col in range(len(two_D[row])):
         print(two_D[row][col], end=' ')
    print()

# use random generator to generate random numbers between 1-100
import random
two_D = []
for i  in range(5):
     row = []
     for j in range(3):
          row.append(random.randint(1,100))
     two_D.append(row)
print(two_D)

# locate the maximum value in two_D
max_value = two_D[0][0]
max_row_idx = 0
max_col_idx = 0 
for row in range(len(two_D)):
     for col in range(len(two_D[row])):
          if max_value < two_D[row][col]:
               max_value = two_D[row][col]
               max_row_idx = row
               max_col_idx = col
print(f'The maximum value in two_D: {max_value} in row {max_row_idx+1} and column {max_col_idx+1}')
flattened_list = [col for row in two_D for col in row]
print(flattened_list)
print(flattened_list.index(max(flattened_list)))
print(flattened_list[0:len(flattened_list):1])
print(flattened_list[3:len(flattened_list):2])
print(flattened_list[-1:-(len(flattened_list)+1):-1])
print(flattened_list[::-1])


             
