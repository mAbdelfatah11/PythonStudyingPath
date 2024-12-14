print("--------------- Dictionary ---------------")

"""
Key-value pair datatype ,====>  colon seperated key value pair
dict is mutable datatype 
non repeated keys 
"""

"1- define dictionary "
d = {}
d2 = dict([])
d3= {"name":"noha", "work":"iti", 1:"september"}
d4 = dict([("track","devops"), ("branch", 'smart')])

"2- get len of the dic"
print(len(d4))

"3- access dic elements using key"
print(d3["name"])

"4- modify dic element using the key"
d3["name"]="Noha Shehab"

"5- add new element to the dict"
d3["birth"] = 1992
print(d3)

"6- remove element from the dic "
# popped = d3.pop("work")
del d3["work"]


"7- update dictionary"
# d3.update(d4)  # add pairs in d4 to d3
# print(d3)
info = {"name":"Ahmed", "city" : "Cairo"}
track_info = {"track":"devops", "branch":"smart", "name":"Magdy"}

track_info.update(info)



"8- get dict keys"
keys = track_info.keys()  # dict_keys
print(list(keys))

"9- get dict values"
values = track_info.values()  # dict_values
print(list(values))


"10- get dict keys, values"
items = track_info.items()  # dict_items
print(items)
print(list(items))

"11- loop over the dic"

# for i in info:   # i ---> represent the key
#     print(f"item = {i}")
#     print(f"item = {i}, value = {info[i]}")
#     print("---------------------------")


for k,v in info.items():
    print(f"{k}: {v}")

"11- get len "
print(len(info))

"12- delete the dict"

# del info

"13- clear dict"

# info.clear()  # remove all the pairs from the dict

"14- check existance "
print("Magdy" in info)  # check if the value exists in the dict keys
print("Magdy" in info.values())