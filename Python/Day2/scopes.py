print("------------- lexical scope ----------------------- ")
"""
    determine the accessibility of the variables in the script 
    
    Any variable in your python script =====> have scope ---> global scope 
"""

""" 1- any variable defined in the script ---> has scope global, can be read 
anywhere in the script  --(inside a function or out side it )  """


"1- global variable"

course = 'Python'

def testScope():
    print(f"inside the function : {course}")

testScope()

"""2- local variable ---> any variable defined inside a function -localscope-
    this varaible can be accessed only in the function 
"""

def askfornum():
    num = input("please enter num")
    if num.isdigit():
        num = int(num)

    print(f"num = {num}")

askfornum()

print(num)

#########################################3
# "3- modify global variable from inside a function"
course=  'mysql'

def changeglobalCourse():
    global course
    course = 'django'
    print(f" inside the function course = {course}")
    course = "python"


changeglobalCourse()

print(f"in the global scope course = {course}")


################################# 'python support function inside a function'

def outerfunction():
    name = 'noha'  # local variable in the function
    def innerfunction():
        print(f"hello {name}")
    innerfunction()


outerfunction()


############### modify the local variable from the inner function
def outerfunction():
    name = 'noha'  # local variable in the function
    def innerfunction():
        name = "Ahmed"  # this new local variable for the innerfunction
        print(f"hello {name}")
    innerfunction()
    print(f"After calling the function:  {name}")

outerfunction()
############################################################

def outerfunction():
    name = 'noha'  # local variable in the function
    def innerfunction():
        nonlocal name   # please don't create new variable use the local one of the outerfunction
        name = "Ahmed"  # this new local variable for the innerfunction
        print(f"hello {name}")
    innerfunction()
    print(f"After calling the function:  {name}")

outerfunction()

















