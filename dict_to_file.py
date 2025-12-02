def write_dict_to_file(filename,data):
    """write to file"""
    with open(filename, 'w') as outfile:
        for key, value in data.items():
            outfile.write(f'{key}:{value}\n')
    print('Writing successfully to file')
def read_from_file(filename):
    """read from file"""
    read_data = {}
    with open(filename, 'r') as infile:
        for line in infile:
            try:
                key, value = line.strip().split(':',1)
                if key == 'bonus':
                    value == float(value)
                read_data[key] = value
            except:
                print(f'Warning:Skipping invalid line format: {line.strip()}')
    return read_data 
def main():
    """main programm"""
    user_data = {
        'user_id':'101',
        'user_name':'JSmith',
        'bonus':450.50
         }
    filename= input('Enter filename:')
    write_dict_to_file(filename,user_data)
    data_loaded = read_from_file(filename)
    print('Original Data', user_data)
    print('Loaded Data', data_loaded)

if __name__ == '__main__':
    main()

