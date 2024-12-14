"""
open the file with mode ---> a append
    ---> append mode ---> if you use it , interpreter will try to the open the file for appending starting
    from the end of the file

    if the file is not exists --> interpreter will try to create it ?
"""



try:
    fileobject=open("files/appenddata.txt", "a")

except Exception as e:
    print(e)
else:
    print(fileobject)  # object ---> TextIOWrapper
    fileobject.writelines(["ahmed\n", "ali\n", 'omar\n', "Mostafa\n"])
    fileobject.close()