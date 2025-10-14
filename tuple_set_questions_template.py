# Tuple challenge questions
'''
Question 1: Data extraction

Given the tuple of nested tuples:
data = (("John", 25, "New York"), ("Jane", 30, "London"), ("Peter", 35, "Paris")).
Write a function that takes this tuple and a name as input. The function should
return the age of the person with that name. If the name is not found, return a message like "Not Found".
'''

data = (("John", 25, "New York"), ("Jane", 30, "London"), ("Peter", 35, "Paris"))
search_name = 'Peter'
def get_age(t,name):
    """return the age of the specified name"""
    for person in t:
        if person[0] == name:
            return person[1]
    return 'Not found'
age = get_age(data, search_name)
if age == 'Not found':
    print(f'Name:{search_name} is not found in the tuple')
else:
    print(f'{search_name} is {age} years old')

        


    
'''
Question 2: Tuple modification (trick question)
You are given the tuple coordinates = (10, 20). Your task is to update the tuple to (10, 30).
What is the correct and most Pythonic way to do this?
'''
coordinates = (10, 20)
coordinates = (coordinates[0], 30)
print(f'Updated coordinates:{coordinates}')

'''
Question 3: Tuple unpacking and concatenation

You have two tuples: t1 = (1, 2, 3) and t2 = (4, 5, 6).
Write a single line of code using tuple unpacking and concatenation to create a new tuple
that contains all elements from t1 and t2 in a single sequence.
'''
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined_t = (*t1, *t2)
print(f'After uppacking: {combined_t}')


'''
Question 4: Nested tuple immutability
Consider the tuple a = (1, 2, [3, 4]).
If you execute a[2].append(5), what will be the value of a? Explain why this happens,
focusing on the concepts of tuple and list immutability.
'''

a = (1,2,[3,4])
a[2].append(5)
print(f'After updating tuple:{a}')


#Set challenge questions

'''
Question 5: Unique elements and sorting
You are given a list with duplicate elements: numbers = [1, 5, 2, 8, 5, 1, 9, 2, 5].

Write a program to:
Convert the list to a set to remove all duplicate numbers.
Convert the set back to a list and sort it in ascending order.
Print the final, sorted, and unique list.
'''

numbers = [1, 5, 2, 8, 5, 1, 9, 2, 5]
numbers_set = set(numbers)
print(f'numbers in set:{numbers_set}')
sorted_list = sorted(list(numbers_set),reverse=True)
print(f'Sorted list in reverse order: {sorted_list}')



'''
Question 6: Set operations for data comparison

You have two sets of students: math_students = {"Alice", "Bob", "Charlie", "David"}
and cs_students = {"David", "Eve", "Frank", "Alice"}.

Write a program to find:
The students who are in both math and CS.
The students who are only in math.
The students who are in either math or CS, but not both.
'''
math_students = {"Alice", "Bob", "Charlie", "David"}
cs_students = {"David", "Eve", "Frank", "Alice"}
print(f'Math students: {math_students}')
print(f'CS students:{cs_students}')


'''
Question 7: Filtering with sets for efficiency
You have a large list of user_ids and a set of banned_ids.
user_ids = [101, 105, 203, 405, 501, 203, 101]
banned_ids = {101, 501}
Write a program that uses a set operation to efficiently find all user_ids
that are not banned. Your solution should use a set, not a loop with an if...in... check for each item
in the list.
'''
user_ids = [101, 105, 203, 405, 501, 203, 101]
banned_ids = {101, 501}


#Combined tuple and set challenge questions

'''
Question 8: Hashable objects in sets
Which of the following can be added to a set in Python and why?
A tuple of numbers: (1, 2, 3)
A list of numbers: [1, 2, 3]
A tuple containing a list: (1, 2, [3, 4])
'''



