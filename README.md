# Project 1
+ By: Mbinintsoa 'Ram' Ramarolahy

# Website description
GoodBooks by GoodReads allows readers to open an account, search for books and see the reviews
and ratings that users left. 
Some future extensions will include creating and joining book clubs where fellow readers
can chat online and talk about their favorite books while sipping matcha!

# Outside resources
+ https://www.w3schools.com/python/default.asp
+ https://scotch.io/@mbithenzomo
+ https://flask-migrate.readthedocs.io/en/latest/
+ http://flask.pocoo.org/docs/1.0/blueprints/
+ https://flask-login.readthedocs.io/en/latest/
+ https://flask-wtf.readthedocs.io/en/stable/quickstart.html
+ https://pythonhosted.org/Flask-Bootstrap/
+ https://wtforms.readthedocs.io/en/latest/index.html
+ https://stackoverflow.com/questions/19699059/representing-directory-file-structure-in-markdown-syntax

# Website Structure
```markdown
project1-ramarolahy
|    
├── app
|   |
|   ├── auth
|   |   ├── __init__.py
|   |   ├── forms.py
|   |   └── views.py
|   ├── home
|   |   ├── __init__.py
|   |   ├── forms.py
|   |   └── views.py
|   ├── static
|   |   ├── css
|   |   |   └── styles.css
|   |   └── img
|   |      └── books.jpeg
|   ├── templates
|   |   ├── auth
|   |   |   ├── login.html
|   |   |   └── register.html
|   |   ├── home
|   |   |   ├── book.html
|   |   |   ├── index.html
|   |   |   ├── profile.html
|   |   |   └── results.html
|   |   ├── includes
|   |   |   ├── banner.html
|   |   |   ├── footer.html
|   |   |   └── navbar.html
|   |   └── base.html
|   ├── __init__.py
|   ├── import.py
|   └── models.py
|
├── flask_session/
├── instance/
├── venv
├── .gitignore
├── config.py
├── README.md
├── requirements.txt
└── run.py
```

# Database Structure

|   TABLE	|   READER	|   BOOK	|   REVIEWS	|
|---	    |---	    |---	    |---    	|
|   READER	|     --   	|    M-M    |    O-M  	|
|   BOOK	|    M-M    |     --	|    O-M  	|
|   REVIEWS	|    O-M  	|    O-M  	|     --  	|

**BOOK**
|   int:ID	|   str:isbn	|   str:title	|   str:author	|   str:year	|

**READER**
|   int:ID	|   str:email	|   str:first_name	|   str:last_name	|   str:password_hash	|

**REVIEWS**
|   int:ID	|   datetime:review_date	|   str:rating	|   str:review_title	|   str:review_text	|   str:book_isbn fk	|   int:reader_id fk	|

**ASSOCIATION**
|   int:reader_id fk	|   str:book_isbn fk	|

# Packages Used
See requirements.txt

# Other Notes
My search feature started acting strange last minute after I did some refactoring. It worked before but now it seems to 
split the search term in to characters and finds all matching results.

I added a feature where readers can see all books they reviewed on their profile page.

On the book page view, the review submitted by the reader will be displayed at the very top.

I did not get time to refactor the search commands to core SQL. Implementing the app with SQLAlchemy allowed me to work faster
and I was planning on refactoring later but ran out of time.

**Active users:**
<br>
<b>User1</b>
<ul>
    <li>email: user1@test.come</li>
    <li>pw: pass1</li>
</ul>
<b>User2</b>
<ul>
    <li>email: user2@test.come</li>
    <li>pw: pass2</li>
</ul>
