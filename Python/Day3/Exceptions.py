print("------------ Exception handling ------------------")
""" 
Exception: unexpected event cause the application to stop 
"""
# print(name)  # interpreted scan the memory and didn't find variable with name name to print
#
# print("----------------- bye---------------------------------")

################################## exception ##############################33
# try:
#     print(name)
# except:
#     print("There is a problem with your process")
#
#
# print("------------------------ bye ----------------------")
#########################################333


# try:
#     # print(course)
#     print(5/0)
# except Exception as e:
#     print(e)
#
#
# print("------------------------ bye ----------------------")

################################# if there is no problem ##########################

# num = input("please enter num")
# try:
#     num = int(num)
# except Exception as e:
#     print(e)
# else:
#     # this block will be executed if there is no problem in the code
#     print("------------------ no problem occured ")
#     print("------- num is casted to int successfully")
#     num = num*2
#     print(num)
#
#
#
# print("------------------------ bye ----------------------")

########################################################3333

# num = input("please enter num")
# try:
#     num = int(num)
# except Exception as e:
#     print(e)
# else:
#     # this block will be executed if there is no problem in the code
#     print("------------------ no problem occured ")
#     print("------- num is casted to int successfully")
#     num = num*2
#     print(num)
# finally:
#     # this block will be exected if there is problem or not ,,,,,
#     print("---------------------- The process completed --------------")
#
#
# print("------------------------ bye ----------------------")

################################## Raising the exception


def divnums():
    num1 = input("please enter num1 ")
    num2 = input("please enter num2 ")
    if num2.isdigit() and num1.isdigit():
        num2 = int(num2)
        if num2==0:
            raise Exception("Division by Zero is not allowed")
        num1 = int(num1)
        res = num1/num2
        return res

r=divnums()
print(r)







