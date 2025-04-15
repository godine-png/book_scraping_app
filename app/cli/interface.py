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
    print("1. Search a book by title")
    print("2. Show info")
    print("3. Exit")
