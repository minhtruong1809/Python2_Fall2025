# Employee Class
class Employee:
    """ A class to represent an employee. """
    def __init__(self, name='', dept='',salary=0.0):
        """ Initialize the employee with name, department, and salary. """
        self.set_name(name)
        self.set_dept(dept)
        self.set_salary(salary)
         
    # getters and setters
    def get_name(self):
        """ Return the name of the employee. """
        return self.__name
         
    def set_name(self, name):
        """ Set the name of the employee. """
        self.__name = name
    def get_dept(self):
        """ Return the department of the employee. """
        return self.__dept
    def set_dept(self, dept):
        """ Set the department of the employee. """
        self.__dept = dept
    def get_salary(self):
        """ Return the salary of the employee. """
        return self.__salary
    def set_salary(self, salary):
        """ Set the salary of the employee. """
        self.__salary = salary
    def __str__(self):
        """ Return employee object as a string. """
        return f'Employee Name: {self.get_name()}, Department: {self.__dept}, Salary: ${self.__salary:.2f}'
    
# test the Employee class
def main():
    """ Main function to test the Employee class and related functions. """
    try:
        emp1 = Employee('J Smith', 'IT', 60000)
        emp2 = Employee('MJones', 'HR', 55000)
        emp3 = Employee('T Cook', 'Finance', 70000)
        emp4 = Employee('J White', 'Marketing', 65000)

        employees = [emp1, emp2, emp3, emp4]
        #call functions
        filename = get_filename()
        write_to_file(filename, employees)
        employee_list = []
        employee_list = read_from_file(filename)
        display_employees(employee_list)
        total_pay = calc_total_salary(employee_list)
        print = (f'Total Salary: ${total_pay:.2f}')


    except FileNotFoundError as fe:
        print(f'Error:{fe}')
    except Exception as ex :
        print(ex)
    else: 
        print(f'All file operations are complete.')
    finally:
        print('Exit the program.')
    
def get_filename():
    """ Prompt for and return a filename. """
    filename = input('Enter the file name:')
    return filename

def write_to_file(filename, emps):
    """ Write employee data to a file. """
    with open(filename, 'w') as outfile:
        for emp in emps:
            outfile.write(f'{emp.get_name()},{emp.get_dept()},{emp.get_salary()}\n')
 
def read_from_file(filename):
    """ Read employee data from a file and return a list of Employee objects. """
    employee_list = []
    with open(filename, 'r') as infile:
        for line in infile:
            name,dept,pay = line.strip().split(',')
            employee_list.append(Employee(name,dept,float(pay)))
    return employee_list
     
def display_employees(emps):
    """ Display a list of employees. """
    for emp in emps:
        print(emp)
    
def calc_total_salary(emp_list):
    """ Calculate and return the total salary of all employees. """
    total_pay = sum(emp.get_salary() for emp in emp_list)
    return total_pay
if __name__ == '__main__':
    main()
