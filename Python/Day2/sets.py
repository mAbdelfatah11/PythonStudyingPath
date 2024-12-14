print("------------------ sets --------------------- ")
""" 
sets is built-in datatype in python ---> don't allow values duplication

--> No index ----> You access individual element
sets ---> unordered datatype 
"""
"1- to define empty set "
s = set([])
"2- sets can hold different datatypes"
mys = {"Ahmed", "Mohamed", "Abdulrahman", "Amira", "Abdulrahman", "Omar", "Ali",2022, 1, "September"}


"3-modify its structure "
mys.add("new item added")
print(mys)

"4-pop element"
popped = mys.pop()

"5- remove element"
mys.remove(2022)

"6- cast it to list or tuple "
mys = list(mys)

l= [4,5,6,4,5,7,8]
l = set(l)
l = list(l)