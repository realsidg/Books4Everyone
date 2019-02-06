# Books4Everyone

This is a book review website. Users are able to register for your website and then log in using their username and password. Once they log in, they will be able to search for books, leave reviews for individual books, and see the reviews made by other people.A third-party API by Goodreads, another book review website,which is used to pull in ratings from a broader audience. Finally, users are also able to query for book details and book reviews programmatically via this website’s API.

## Features of the Web Application 

### Registration: 
Users are be able to register for your website, providing (at minimum) a username and password.

### Login: 
Users, once registered, are be able to log in to your website with their username and password.

### Logout: 
Logged in users are be able to log out of the site.

### Search: 
Once a user has logged in, they are be taken to a page where they can search for a book. Users are be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page can find matches for those as well!

### Book Page: 
When users click on a book from the results of the search page, they are be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.

### Review Submission: 
On the book page, users are be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users are not be able to submit multiple reviews for the same book.

### Goodreads Review Data: 
On book page, it displays (if available) the average rating and number of ratings the work has received from Goodreads.

### API Access: 
If users make a GET request to website’s /api/<isbn> route, where <isbn> is an ISBN number, website returns a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON follows the format:
```
{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}
```

### And much more! 

## Getting Started

### Prerequisites

- You should have python 3+ and pip installed.
- Go to project1 directory and run this command to install all required python modules needed. 

```
pip install -r "requirements.txt"
```

### Installing

- Set your environment variable DATABASE_URL to your desired postgresSQL URI
- Run the import.py file in order to create tables and import the csv to your database 
```
python import.py
```

## Deployment

```
flask run
```
