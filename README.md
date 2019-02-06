# Books4Everyone

This is a book review website. Users are able to register for your website and then log in using their username and password. Once they log in, they will be able to search for books, leave reviews for individual books, and see the reviews made by other people.A third-party API by Goodreads, another book review website,which is used to pull in ratings from a broader audience. Finally, users are also able to query for book details and book reviews programmatically via this website’s API.

## Features of the Web Application 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

-You should have python 3+ and pip installed.
-Go to project1 directory and run this command to install all required python modules needed. 

```
pip install -r "requirements.txt"
```

### Installing

-Set your environment variable DATABASE_URL to your desired postgresSQL URI
-Run the import.py file in order to create tables and import the csv to your database 
```
python import.py
```

## Deployment

```
flask run
```
