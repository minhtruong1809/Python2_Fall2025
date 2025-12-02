# selection sort
# iterative approach
def selection_sort(lst):
    """selection sort using iterative approach"""
    size = len(lst)
    for i in range(size):
        min_index = i 
        for j in range(i+1, size):

            if lst[j] < lst[min_index]:
                min_index = j
        lst[i],lst[min_index] = lst[min_index],lst[i]
    return lst
# recursive selection sort
def selection_sort_re(lst, start_index=0):
    """recursive selection sort"""

    if start_index >= len(lst)-1:
        return 
    min_index = start_index
    for j in range(start_index+1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[start_index], lst[min_index] = lst[min_index], lst[start_index]
    return selection_sort_re(lst, start_index+1)

def selection_sort_re_with_helper(lst):
    """selection sort with helper function"""
    sort_helper(lst, 0, len(lst))
def sort_helper(lst, start_index, size):
    """helper function"""
    if start_index >= size -1:
        return
    min_index = start_index
    for j in range(min_index+1, size):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[start_index], lst[min_index] = lst[min_index], lst[start_index]
    sort_helper(lst, start_index+1, size)
#binary search iterative
def binary_search(lst, target):
    """iterative binary search"""
    left, right=0, len(lst)-1
    while left <= right :
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return -1         

# binary search recursive
def binary_search_re(lst, target):
    if len(lst) == 0:
        return -1
    mid = len(lst) // 2 
    if lst[mid] == target :
           return mid
    elif lst[mid] < target:
        return binary_search_re(lst[mid+1:],target)
    else:
        return binary_search_re(lst[:mid],target)
    



import random
def main():
    """main program"""
    random.seed(12345)

    lst = [random.randint(1,100) for _ in range(10)]
    print(f'Original list: {lst}')

    # call iterative selection sort
    lst_copy = lst.copy()
    #selection_sort(lst_copy)
    print(f'Selection sort in iterative approach:{selection_sort(lst_copy)}')

    lst_copy = lst.copy()
    selection_sort_re(lst_copy)
    print(f'Selection sort in recursive approach:{lst_copy}')

    lst_copy = lst.copy()
    selection_sort_re_with_helper(lst_copy)
    print(f'Selection sort in recursive approach:{lst_copy}')

    lst = [num for num in range(1,16)]
    lst_copy = lst.copy()
    search_value = 8
    index = binary_search(lst,search_value)
    print(f'{search_value} is in index:{index}')
    
    index = binary_search_re(lst,search_value)
    print(f'{search_value} is in index:{index}')


if __name__ == '__main__':
    main()

