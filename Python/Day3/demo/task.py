

""" library --> books
    file ---> all information books
    book title, book description, year, id

    -------> console application
    ===> CRUD operations on the books
    Create
    list , update , delete

"""
from bookhandler import createBook, listallbooks, deletebook, editbook
def mainmenu():
    choice = input("""please enter choice
c ---> create
l ---> list: 
e ---> edit 
d ---> delete: """)

    if choice in ["c", "l", "e", "d"]:
        if choice=='c':
            createBook()
        elif choice=='d':
            deletebook()
        elif choice=='e':
            editbook()
        else:
            listallbooks()
    else:
        print("------------ please choose suitable option ------------------")
        return mainmenu()


mainmenu()







