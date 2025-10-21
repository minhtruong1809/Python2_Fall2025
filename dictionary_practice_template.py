# dictionary practice

# 1. create dictionary from python list

fruits = ['apple', 'banana', 'cherry']
qty = [10, 20, 30]

fruits_dict = dict(zip(fruits,qty))
print(f"After zipping:{fruits_dict}")

# 2. sum dictionary values

items_dict = {'item1': 45.50, 'item2': 35, 'item3': 41.30}

total_value = sum(items_dict.values())
print(f'Total value: ${total_value}')


# 3. write a function to check if key is in a dictionary

person = {'name': 'JSmith', 'age': 55, 'city': 'Houston'}
key_to_check = 'age'
def  check_key(d,key):
    """check whether key arguement is in dict"""
    return key in d
key_existed = check_key(person, 'age')
print(f'age in dict:{key_existed}')




# 4. combine two dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(f'After merging: {dict1}')
dict3 = dict1 | dict2
print(f'After merging using |: {dict3}')
dict4 = {**dict1, **dict2}
print(f'After merging using unpacking:{dict4}')

 

# 5. giving a string, check frequency of each character

text = input('Enter a string:').strip().lower()
frequency = {}
for ch in text:
    if ch.strip(' .,?'):
        if ch in frequency:
         '''''
            frequency[ch] += 1
        else:
            frequency[ch] = 1
         '''''
        frequency[ch] = frequency.get(ch,0) + 1
    

for key in frequency:
    print(f'{key}: {frequency[key]}')

text = input('Enter a string:').lower()

frequency = {}


 


# 6. Inverted key, value pair

original = {'a': 1, 'b': 2, 'c': 1,'d':3, 'e':3}
inverted = {}
for key, value in original.items():
    if value not in inverted:
       inverted[value] = [key]
    else:
      inverted[value].append(key)

print(f'Original dict:{original}\nInverted dict:{inverted}')

      


        
# 7. locate key contains the largest value
salsa_sales = {'Mild':10, 'Medium':30, 'Hot': 5, 'Zesty':25}

flavor_max_jars = max(salsa_sales,key=salsa_sales.get)
print(f'Flavor with most jars sold: {flavor_max_jars}')




# 8. access nested dictionary - change the quantity of corolla to 20
inventory = {
    'cars': {
        'Ford': {'focus': 10, 'mustang': 5},
        'Toyota': {'camry': 15, 'corolla': 12}
    }
}
inventory['cars']['Toyota']['corolla'] = 20
print(inventory)
