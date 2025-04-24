#Creates the visual elements of the CLI interface

def welcome():
    # This function prints a welcome message to the user.
    # It should be called when the program starts.
    print("##############################################################")
    print("#                                                            #")
    print("#                      BOOK SCRAPER                          #")
    print("#                                                            #")
    print("##############################################################")
    options()

def options():
    #Shows main menu
    print("1. Search a book by title")
    print("2. Exit")

def bookList(cards):
    # Shows list of books
    i = 1
    for book in cards:
        print(f"{++i}. {book["title"]}")
        i+=1
