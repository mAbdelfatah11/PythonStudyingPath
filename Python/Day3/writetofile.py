

"""
open the file with mode ---> w
    ---> write mode ---> if you use it , interpreter will try to the open the file for writing starting
    from the beginning of the file (remove existing content)

    if the file is not exists --> interpreter will try to create it ?
"""

####################### write to a file
# try:
#     fileobject=open("files/mycv.txt", "w")
#
# except Exception as e:
#     print(e)
# else:
#     print(fileobject)  # object ---> TextIOWrapper
#     fileobject.write("My name is Ahmed\n")
#     fileobject.write("I works at iti")
#
#     fileobject.close()

##################################

try:
    fileobject=open("files/mycv.txt", "w")

except Exception as e:
    print(e)
else:
    print(fileobject)  # object ---> TextIOWrapper
    fileobject.writelines(["ahmed\n", "ali\n", 'omar\n', "Mostafa\n"])
    fileobject.close()