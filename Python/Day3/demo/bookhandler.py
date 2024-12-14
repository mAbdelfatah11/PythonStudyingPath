import time
from filehandler import createnewBook, getallbooks, deleteBookFromFile, searchbookbyId, updateBookinfile


def askforvalidStr(message):
    value = input(message)  # ""
    if value.isdigit() or value.isspace() or not value:
        print("---------------- please enter correct value for string -------")
        return askforvalidStr(message)

    return value


# ###############################################################3
def askforvalidInt(message):
    value = input(message)
    if value.isdigit():
        return int(value)
    print("---------------- please enter correct value for int -------")
    return askforvalidInt(message)


# ###############################################################3
def basicbookInfo():
    title = askforvalidStr("Please enter book title: ")
    description = askforvalidStr("Please enter book description: ")
    year = askforvalidInt("Please enter year of publication: ")
    return title, description, year


# ###############################################################3
def createBook():
    print("======== create book ==========")
    book_details = basicbookInfo()
    # uuid # timestamp
    book_id = str(round(time.time()))
    # print(book_details)
    ######
    bookinfo = f"{book_id}:{book_details[0]}:{book_details[1]}:{book_details[2]}\n"
    # print(bookinfo)
    added = createnewBook(bookinfo)
    if added:
        print("----- New book created -------------- ")


# ###############################################################3
def listallbooks():
    books = getallbooks()
    print("-------------- All books --------------- ")
    print(books)


# ###############################################################3
def deletebook():
    listallbooks()
    book_id = askforvalidInt("please enter the id of the book you want to delete: ")

    # search all books that contian this ide --->
    deleted = deleteBookFromFile(book_id)
    if deleted:
        print("Book deleted successfully ")
        print("------------------------------------------")
        listallbooks()


# ###############################################################3
def editbook():
    listallbooks()
    book_id = askforvalidInt("please enter the id of the book you want to edit: ")
    book_index = searchbookbyId(book_id)
    print(book_index)
    if book_index or book_index == 0:
        print("----------------- edit the book info --------------- ")
        book_data = basicbookInfo()
        print(book_data)
        updated_book = f'{book_id}:{book_data[0]}:{book_data[1]}:{book_data[2]}\n'
        # send this data to the file
        updated = updateBookinfile(book_index, updated_book)
