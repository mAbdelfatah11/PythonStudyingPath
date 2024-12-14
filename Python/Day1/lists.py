print("----------- lists ------------------- ")

"1- to define a list "
l = []
newl = list([])

"2- list can hold different values from different datatypes"
myl = ["python", 1, 43, "devops", "smart village", ["django", "mysql"], "python"]

"3- count element in the list"

print(myl.count("python"))

"4- access elements through the index"
print(myl[3])

"5- list are mutable datatypes  ---> you can update its content after creation "
myl[2]="intake 43"

# "6- add item to non-existing index "
# myl[10]= "new item "  # list assignment index out of range

"6- append item to the list ---> add to the end "
myl.append("new item")

"7- insert new item ---> at certain index "
myl.insert(4, "inserted")

"8- pop the last element "
item = myl.pop()

"9- pop  element  at certain index"
item = myl.pop(4)

"10- remove element "
myl.remove("python")  # remove the first occurrence of the elements

"11- list concatenation "
# l1 = ["python", "django"]
# l2 = ["flask", "odoo"]
# l3 = l1 + l2
# print(l3)

"12- extend list "
l1 = ["python", "django"]
l2 = ["flask", "odoo", "python"]
l1.extend(l2)

"13- sort the list ---> list items must form the same type"
# l1.sort()
# l1.sort(reverse=True)

"14- reverse the list"
l1.reverse()

"15- loop over the list item "
# for item in l1:
#     print(item)


"16- min , max ==> all items in the list must be from the same type "
print(min(l1))


"17- check existance "
print("python" in l1)