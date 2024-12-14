def writeAllbooks(books):
    try:
        filobject = open("books.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        filobject.writelines(books)
        return True

def createnewBook(book):
    try:
        filobject = open("books.txt", "a")
    except Exception as e:
        print(e)
        return False
    else:
        filobject.write(book)
        return True



def getallbooks():
    try:
        filobject = open("books.txt", "r")
    except Exception as e:
        print(e)
        return False
    else:
        books = filobject.readlines()
        return books


def searchbookbyId(book_id):
    # check if the book in the file
    allbooks=getallbooks()
    for book in allbooks:
        book_details = book.split(":")
        if book_details[0]==str(book_id):
            # print("found")
            book_index = allbooks.index(book)
            return book_index
    else:
        return False

def deleteBookFromFile(book_id):
    book_index = searchbookbyId(book_id)
    allbooks = getallbooks()
    del allbooks[book_index]
    ## write the new list to the file
    deleted = writeAllbooks(allbooks)
    return deleted


def updateBookinfile(book_index, book_data):
    allbooks = getallbooks()
    allbooks[book_index]= book_data
    updated= writeAllbooks(allbooks)
    return updated



