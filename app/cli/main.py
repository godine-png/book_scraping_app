# Terminal Interface

# Run this file using 'uv run -m app.cli.main'
"""
from app.core.extractor import
from app.core.models import
from app.core.scrapper import
"""

from app.core.hello import helloWorld
import app.core.scrapper as sc 
import app.cli.interface as ti
import app.core.extractor as ex
import app.core.models as md


def run():
    # Main Terminal Interface logic here
    finish = False
    ti.welcome()
    while not finish:
        x = input("Enter a value: ")
        if x == "1":
            # Placeholder for book search functionality
            print("Searching for a book...")
            search()
        elif x == "2":
            # Placeholder for showing info functionality
            print("Showing info...")
            info()
        elif x == "3":
            print("Exiting the program...")
            finish = True
            break
        else:
            print("Invalid option. Please try again.")
        print("returning to main menu...")
        ti.options()
    #helloWorld()
    sc.default()

def search():
    # Placeholder for book search functionality
    print("This function will search for a book by title.")

def info():
    # Placeholder for showing info functionality
    print("This function will show information about the book.")


if __name__ == "__main__":
    run()
