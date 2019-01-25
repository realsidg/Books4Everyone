import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# engine = create_engine('postgres://wglpsxsnsywagl:4eedef15980f1b3c30ad03ccab9b7521512d10f83a46425176e4058faa3952ea@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d2e7hjk3067394')


engine = create_engine(os.getenv('DATABASE_URL'))
# engine.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY, title varchar, author varchar, year integer);")

db= scoped_session(sessionmaker(bind=engine))

f=open("books.csv",)
reader=(csv.DictReader(f))
ctr=0
for field in reader:
    db.execute(f"INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {'isbn':field['isbn'], 'title':field['title'],'author':field['author'],'year':field['year']})
    print("Inserted: ",field)

db.commit()