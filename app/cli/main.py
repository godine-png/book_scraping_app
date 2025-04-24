# Terminal Interface

# Run this file using 'uv run -m app.cli.main'
"""
from app.core.extractor import
from app.core.models import
from app.core.scrapper import
"""
from bs4 import BeautifulSoup
from app.core.hello import helloWorld
import app.core.scrapper as sc 
import app.cli.interface as ti
import app.core.extractor as ex



def run():
    # Main Terminal Interface logic here
    finish = False
    ti.welcome()
    cards = sc.default()
    #Reads cards, only intended to print for testing
    """
    for card in cards:
        print("-"*75)
        print(card["title"])
        print("Authors:")
        for item in card["authors"]:
            print(item.text)
    """
    while not finish:
        x = input("Enter a value: ")
        if x == "1":
            #Shows info of a selected book
            ti.bookList(cards)
            enter = input("Enter a book: ")
            print("Searching for a book...")
            search(enter, cards)
        elif x == "2":
            print("Exiting the program...")
            finish = True
            break
        else:
            print("Invalid option. Please try again.")
        print("returning to main menu...")
        ti.options()
    #helloWorld()
    

def bookPrinter(card):
    #prints book card
    print("-"*75)
    print(card["title"])
    print("Authors:")
    for item in card["authors"]:
        print(item.text)
    print("-"*75)

def search(title, cards):
    #searches for a book card based on title
    match = False
    for book in cards:
        if book["title"] == title:
            bookPrinter(book)
            match = True
    if match == False:
        print("Error 404: Book Not Found :(")

if __name__ == "__main__":
    run()
