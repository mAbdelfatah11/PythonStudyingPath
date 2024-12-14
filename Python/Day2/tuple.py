print("------------- tuples-------------")
"""tuple is one of built in datatype
like lists---> 

tuple is immutable  ========> you can not append or update values, that is the most important thing and the differnce between tuple and list
"""

"1- to define a tuple "
t = ()
newt = tuple([])

"2- tuple can hold different values from different datatypes"
myt = ("python", 1, 43, "devops", "smart village", ["django", "mysql"], "python")


"3- count element in the tuple"
print(myt.count("python"))

#### no availaibitly for append or insert 

"4- access elements through the index"
print(myt[3])

"5- tuple concatenation ---> this a new one "
t1 = ("python", "django")
t2 = ("flask", "odoo")
t3 = t1 + t2
print(t3)


"6- loop over the tuple items "
for item in t1:
    print(item)

"7- min , max ==> all items in the tuple must be from the same type "
print(min(t1))


"8- check existance "
print("python" in t1)


"9- casting to list and vise versa "

names = ("Kareem", "Abdulrahman", "Omar", "Ali", "Amira", "Kerolous")
names = list(names)
print(type(names))   # list

names = ["Kareem", "Abdulrahman", "Omar", "Ali", "Amira", "Kerolous"]
names = tuple(names)
print(type(names))   # tuple



####################################3
"10- delete variable from the memory "
# del myt  # delete variable from memory in the runtime
myt = list(myt)
del myt[5]








