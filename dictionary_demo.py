d = {}
print(f'Type of d: {type(d)}')
# empty set
s = set()
d = {1: 'one',2: 'two',3:'three'}
print(f'display d:{d}')
num_dict = {k:k*2 for k in range(1,11)}
print(f'number dict: {num_dict}')
#acces value from key
print(f'd[1] = {d[1]}')
print(f'd[4] = {d.get(4,"Key does not exist.")}')
#remove key/value pair
print(f'popping item = {d.pop(4, "Key does not exist")}')
d1 = {1:'one',2:'two',3:'three'}
d2 = {3:'3',4:'four'}
d1.update(d2)
print(f'After updating, d1={d1}')
#d1[3] = '3'
d3 = d1.update(d2)
print(d3)
#use different merge method/operator
d4 = d1 | d2
print(f'd4 = {d4}')
d5 = {**d1, **d2}
print(f'd5 = {d5}')
# traverse dictionary
for key, value in d5.items():
    print(f'{key}:{value}')
for key in d1.keys():
    print(key, end= ' ')
print()
for key in d1.keys():
    print(f'{key}, {d1[key]}')
# add values
sales = {'Item1':20.0,'Item2':43.5,'Item3':109.0}
total = 0.0
for value in sales.values():
    total += value
print(f'Sum of values:{total}')
total = sum(sales.values())
print(f'total = {total}')
# reverse the key/value pair
d6 = {}
for key, value in d1.items():
    d6[value] = key
print(f'After reversing key/value pair:{d6}')
# another example using zip()
objects = ['blue','apple','dog']
category = ['color','fruit','pet']
obj_dict = {key:value for key,value in zip(category,objects)}
print(f'After zipping:{obj_dict}')
print(dict(zip(category,objects)))