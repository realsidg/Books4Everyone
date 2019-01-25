import os
import requests
import re
import hashlib

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def Validate(name, email, user, passw, repeatpass):
    message=""
    check=True
    if not (re.match("^[a-zA-z ]+$",name)):
        check=False
        message="Invalid Name"
        
    if check and not (re.match("^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$",email)):
        check=False
        message="Invalid Email"
    else:
        for u in db.execute("SELECT email from USERS").fetchall():
            if re.match(u[0],email,re.I):
                check=False
                message="Email aldready exists"

    if check and not (re.match("^[a-zA-z0-9_]*$",user)):
        check=False
        message="Invalid Username"
    else:
        for u in db.execute("SELECT username from USERS").fetchall():
            if re.match(u[0],user,re.I):
                check=False
                message="Username aldready exists"
        
    if check and not (re.match("^[A-Za-z0-9@#$%^&+=]{8,}$",passw)):
        check=False
        message="Invalid Password"

    if check and not  passw==repeatpass:
        check=False
        message="Passwords do not match"
    
    if check:
        passw=hashlib.md5(passw.encode()).hexdigest()
        db.execute("INSERT INTO users (name, email, username, passw) VALUES (:name, :email, :username, :passw);",{'name':name, 'email':email,'username':user,'passw':passw})
        db.commit()
        message="Registered Successfully"

    return (message, check)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def books():
    data=""
    isbn=request.args.get('query')
    if isbn is not None:
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "fcJPItrdhaNf8KQuAd1bQ", "isbns": isbn})
        data=res.json()
    return render_template("book_details.html", data=data)

@app.route("/signup",methods=['POST','GET'])
def signup():
    message=""
    check=None
    if request.method=="POST":
        message, check= Validate(request.form.get("name"), request.form.get("email"),request.form.get("user"), request.form.get("pass"), request.form.get("repeatpass"))

    rang = "green" if check else "red"
    return render_template("signup.html",message=message,rang=rang)

@app.route("/login",methods=['GET','POST'])
def login():
    check=False
    if request.method == "POST" :
        for usr in db.execute("SELECT username from USERS").fetchall():
            if re.match(usr[0],request.form.get('username'),re.I):
                check=True

        if check:
            check=False
            for usr in db.execute("SELECT passw from USERS").fetchall():
                if re.match(usr[0], hashlib.md5(request.form.get('password').encode()).hexdigest()):
                    check=True

    return render_template("login.html", check=check)
