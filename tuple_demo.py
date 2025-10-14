#  tuple  demo

def add_to_tuple(t,  value):
    '''check each element in tuple to determine whether the element is mutable'''
    for element in  t:
        if type(element) is list:
            element.append(value)
        elif type(element) is tuple:
            print(f'Tuple is immutable.')
        elif type(element) is set:
            element.add(value)
        elif type(element) is dict:
            print('Need key to modify the dictionary. ')

        else:
            print(type(value))
            
t1 = ([1,2],('Apple','Orange'),{5,11},{1:'one',2:'two'},78)
add_to_tuple(t1,67)
print(t1)