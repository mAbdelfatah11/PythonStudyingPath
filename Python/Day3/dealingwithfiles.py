print("------------------------ dealing with files ---------------- ")

"""
    1- open file ---> decide the operation you need to do on the file 
        (read , write, append)
        use  open(filename, mode)
        mode ----> r (read) , w (write) ---> write , a (append) ---> write in file --> at the end of the file
    
    2- do the operation (read , write)
    
    3- close the file 
"""

############################# Read #######################################

# try:
#     # fileobject=open("files/students.txt", "r")
#     fileobject=open("files/students.txt")
#
# except Exception as e:
#     print(e)
# else:
#     print(fileobject)  # object ---> TextIOWrapper
#     ### read file content
#     data = fileobject.read()  #read file content into on string
#     print(data)
#
#     fileobject.close()
#



# #######################3 Read file line by line
# try:
#     # fileobject=open("files/students.txt", "r")
#     fileobject=open("files/students.txt")
#
# except Exception as e:
#     print(e)
# else:
#     print(fileobject)  # object ---> TextIOWrapper
#     ### read file content
#     data = fileobject.readline()  #read line from the file
#     print(data)
#     data = fileobject.readline()  # read line from the file
#     print(data)
#
#     fileobject.close()


#######################3 Read file line by line into a list
# try:
#     # fileobject=open("files/students.txt", "r")
#     fileobject=open("files/students.txt")
#
# except Exception as e:
#     print(e)
# else:
#     print(fileobject)  # object ---> TextIOWrapper
#     ### read file content
#     data = fileobject.readlines()  #read file content line by line and put them in a list
#     print(data)
#     fileobject.close()


#######################33 line by line
#######################3 Read file line by line
try:
    # fileobject=open("files/students.txt", "r")
    fileobject=open("files/students.txt")

except Exception as e:
    print(e)
else:
    for l in fileobject:  # loop over the file object.
        print(l)

    fileobject.close()













