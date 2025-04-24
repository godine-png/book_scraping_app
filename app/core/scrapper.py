# Handle HTTP Requests and HTML Parsing to get book data using requests and beautifulsoup4
from bs4 import BeautifulSoup
from app.core.models import card
import requests as req


def default():
    #Creates a list to be read by Main
    cards = []
    # The list is imited for now, possibility of adding a way to look a book up, if so the app might be redesigned for Google Books
    cards.append(request("https://www.goodreads.com/book/show/212979306-the-ultimates-by-deniz-camp-vol-1"))
    cards.append(request("https://www.goodreads.com/book/show/44767458-dune?ac=1&from_search=true&qid=dysI94xO6S&rank=1"))
    cards.append(request("https://www.goodreads.com/book/show/56916837-to-kill-a-mockingbird"))
    return cards
def request(url):
    #Performs the request and separates to the dictionary
    loCard = card.copy()
    webpage = req.get(url)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    #Must add implementation to avoid duplicates
    #This part should be moved to the extractor eventually
    loCard["authors"] = soup.find_all('span', class_='ContributorLink__name')
    loCard["title"] = soup.h1.string
    return loCard