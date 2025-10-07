# write random numbers to file, read the file and calculate the sum/average of the numbers
import random

def main():
    """ main functions"""
    file_name = get_filename()
    write_to_file(file_name)
    num_list = read_from_file(file_name)
    print(f'The origianl list : {num_list}')
    total, average = calculate_sum_average(num_list)
    print(f'Sum = {total}, Average= {average:.2f}')
    largest_idx = get_largest_idx(num_list)
    print(f'The largest number {num_list[largest_idx]} is stored in index {largest_idx}')



def get_filename():
    """ get filename from user """
    filename = input('Enter the file name:')
    return filename


def write_to_file(filename):
    """ write random numbers to file """
    with open(filename,'w') as outfile:
        for i in range(10):
            number = random.randint(1,100)
            outfile.write(f'{number}\n')
    
    print(f"Random numbers written to {filename}")

def read_from_file(filename):
    """ read numbers from file and return as a list """
    with open(filename,'r') as infile:
       #numbers = [int(line) for line in infile]
        numbers = [] 

        for line in infile:
            numbers.append(int(line))
    return numbers
    

def calculate_sum_average(numbers):
    """ calculate sum and average of a list of numbers """
    # total = sum(numbers)
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return total, average   

def get_largest_idx(numbers):
    """find the index that holds the largest number in list"""
    idx = 0
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[idx]:
            idx = i
        return idx
if __name__ == '__main__':
    main()