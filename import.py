import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db= scoped_session(sessionmaker(bind=engine))

db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY, title varchar, author varchar, year integer);")

f=open("books.csv",)
reader=(csv.DictReader(f))
ctr=0
for field in reader:
    db.execute(f"INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {'isbn':field['isbn'], 'title':field['title'],'author':field['author'],'year':field['year']})
    print("Inserted: ",field)

db.commit()