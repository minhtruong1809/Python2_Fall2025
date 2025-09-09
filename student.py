# student class to keep track student's grades
class Student:
    """ student class to keep track student's grades """
    # initialization
    def __init__(self,name='',grades=[]):
        """ initializer/constructor """
        self.name = name
        self.grades = grades
    # getters/setters
    def get_name(self):
        """ return student's name """
        return self.name
    def set_name(self,name):
        """ set student's name """
        self.name = name
    def get_grades(self):
        """ return student's grade """
        return self.grades 
    def set_grades(self,grades):
        """ set student's grades """
        self.grades = grades 

    # methods 
    def calc_average(self):
        """ calculate the student's average """
        return sum(self.grades)/ len(self.grades)
    def __str__(self):
        """ display object in a string """
        return f"Student Name:{self.name} Student's Average: {self.calc_average():.2f}"
# test class
if __name__ == '__main__':
    student1 = Student('John Smith',[80,90,100])
    print(student1)
    student2 = Student()
    student2.set_name('Mary Jones')
    student2.set_grades([60,75,95])
    print(student2)
    
    #create a list of student object 
    students = [student1,student2]
    for student in students:
        print(student)








