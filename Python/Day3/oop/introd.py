print("------------------------OOP----------------------------------------")

# emp1 ={
#     "name" : "ahmed",
#     'email' : "ahmed@gmail.com",
#     "dept" : "devops"
# }
#
# emp2 ={
#     "empname" :"ali",
#     'empemail': "ali@gmail.com",
#     "dept" : "sd"
# }

"""
    abobe u have created two different dictioners with two different key names, which introduces inconsistent rules
"""

"""
    belwo, i will create my own datastructure Employee ---> name, email , dept , id 

    define class which is the blueprint for a specific structure in which u define
    --> properties of the instances or objects that will be created from this class
    --> functionalities these instances can do 
"""
# ##############3 create class ########################
# class Employee:
#     pass


# print(Employee)          # Shows <class '__main__.Employee'>, indicating the main class object since you have not created any class objects yet



#############################################

##############3 create object or class instance ########################
# class Employee:
#     def __init__(self):  # constructor function ---> the first function called while creating the object "class instance"
#         print(self)   # Prints the [memory address] of the current called object "optional" 
#                       # self --> refer to the address of the current caller instance , example: when u create object, self is ur gate to access the class, actually it's the object or the class instance address in the memory
#         self.name = "emp"    # Defines instance variable, will be the variable applied for each object who calls this class
#         self.email = "ahmed@gmail.com"
#         self.id = 10


# e = Employee()  # Creates the first instance of Employee
# print(e)  # Prints the address of e, same as above
# e2 = Employee()  # Creates a second instance with its own memory address

#######################3 customize the object creation
#
# class Employee:
#     def __init__(self,name, email,id):  # make the instance variable dynamic, not statically applied in the __init__ function
#         print(self)   # Prints the [memory address] of the current called object "optional" 
#         self.name = name  # instance varaible
#         self.email = email
#         self.id = id
#
#
# e = Employee("Ahmed", "ahmed@gmail.com", 10)  # address of object

# python support representing the object in form of dictionary.
## When you define a class in Python, it creates a __dict__ attribute, which is a dictionary that stores all the attributes and methods defined within the class. This __dict__ is often called the namespace of the class.
###  The __dict__ dictionary is a useful way to inspect what is available within a class and class object

# print(e.__dict__)
# e2 = Employee("Ali", "ali@gmail.com", 4)
# print(e2.__dict__)
#
#
# # ######################## instance method
#
# class Employee:
#     def __init__(self,name, email,id):  # constructor function ---> is called while creating the object
#         print(self)   # Prints the [memory address] of the current called object "optional" 
#         self.name = name  # instance varaible
#         self.email = email
#         self.id = id
#
#     # instance method
#     def printEmpInfo(self): # self ---> refer to the current caller instance
#         print(f"my name is {self.name}, you can reach me at {self.email}")
#
#
# e = Employee("Ahmed", "ahmed@gmail.com", 10)  # address of object
# e.printEmpInfo()
# e2 = Employee("Ali", "ali@gmail.com", 4)
# e2.printEmpInfo()
#
#


############################# class variable

# ######################## instance method
"""propery value ---> shared between all instance ---> it depends on the Class not the instance 

You can access it using class Name 
"""


class Employee:
    nationality = "Egyptian"   # class variable ---> value depends on the class not the object

    def __init__(self, name, email, id):  # constructor function ---> is called while creating the object
        print(self)  # self --> refer to the object address in the memory
        self.name = name  # instance varaible
        self.email = email
        self.id = id

    # instance method
    def printEmpInfo(self):  # self ---> refer to the current caller instance
        print(f"my name is {self.name}, you can reach me at {self.email}")

e = Employee("Ahmed", "ahmed@gmail.com", 10)  # address of object
e2 = Employee("Ali", "ali@gmail.com", 4)
e3 = Employee("Mohmed", "ali@gmail.com", 4)
print(e3.nationality)


