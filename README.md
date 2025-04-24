# Book Scraping App

This application which takes in user input for a book, then scrapes Goodreads or
related sites to find common descriptors/ summaries to showcase the types of
books you read.

The main core uses:

- [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [requests](https://pypi.org/project/requests/)
- [spacy](https://spacy.io/usage/spacy-101)
to gather and parse the book data.

## Setup

This project uses [uv](https://github.com/astral-sh/uv). Ensure that you have uv
installed.

Run:

`uv venv`

`.venv/Scripts/activate`

`uv pip install .`

`uv run -m app.cli.main`

GDG Mentorship Technical Project Spring 2025
