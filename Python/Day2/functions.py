print("--------------- functions ---------------------------")

""" ------------------------ functions with known number of arguments -----------"""
"1- basic function"
# def getfullname():
#     firstname = input("please enter your firstname : ")
#     lastname = input("please enter your last name :  ")
#     print(f"fullname : {firstname} {lastname}")
#
# getfullname()
#
# getfullname()

########################################3333
"2- function accept arguments "
# def sumnum(num1, num2):
#     res = num1  +  num2
#     print(res)
#
#
# sumnum(10, 20)

######################################## the diffwerence between return and print #######
# "3- function that returns with a value "
#
#
def sumnum(num1, num2):  # num1 , num2 Arguments
    res = num1 + num2
    return res


r = sumnum(44, 555)  # 44, 555--> parameters
print (r)


# function with print:

def add_numbers(a, b):
    print(a + b)

sum = add_numbers(5, 3)  # Output: 8
print(sum)  # Output: None

# - the difference here:
# - return: Gives back a value that you can store, use, or manipulate later.
# - print: Only displays the output on the screen; it does not allow further use of the value.


##################################################

"""  default arguments"""

# def sumnum(num1, num2=100):
#     print(f"num1= {num1}, num2 = {num2}")
#     res = num1 + num2
#     print(res)
#
# sumnum(10)
#
# sumnum(55, 44)
#
# sumnum("iti", "devops")
#
# sumnum("iti",10)

######################################
#
# def sumnum(num1 :int, num2 :int):  # this helper syntax
#     # isinstance
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1= {num1}, num2 = {num2}")
#         res = num1 + num2
#         print(res)
#         return res
#     return
#
#
# sumnum(10, 20)
#
# sumnum(55, 44)

# sumnum("iti", "devops")

# sumnum("iti",10)

########################################
# x = 10
# if type(x)=='int':
#     print('matched')
# else:
#     print("not matched")
#
# xtype = type(x)   # object from class type
# print(xtype, type(xtype))


# x = 100
# if type(x) == type(10):
#     print("matched")
# else:
#     print("not matched")


############################################# ####################################

""" function accept unknown number of arguments """

#
# def sumnumbers(*numbers):  # accept zero or more arguments
#     print(numbers)  # tuples
#     print("-----------------")
#
#
# sumnumbers()
# sumnumbers(2, 5, 4)
# sumnumbers(4)

###########################
#
def introduce_your_self(**kwargs):
    print(kwargs)
    print("----------------------")



introduce_your_self(name="noha", work='iti')
# introduce_your_self()
# introduce_your_self(firstname='ahmed', secondname='ali', sep='engineering', city='cairo')


x = 10
y = 'iti'
z = 'python'

print(x,y,z)



temp = "My name is {username} , I works at {work}, {test}"

print(temp.format(username="noha", work="iti", test=""))
print(temp.format(username="Ahmed", work="Devops",test=""))
