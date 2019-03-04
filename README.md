# Project 1
+ By: Mbinintsoa 'Ram' Ramarolahy
+ Production URL: <url>

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
├── flask_session/
├── instance/
├── venv
├── .gitignore
├── config.py
├── README.md
├── requirements.txt
└──run.py
```

# Database Structure

|   TABLE	|   READER	|   BOOK	|   REVIEWS	|
|---	    |---	    |---	    |---    	|
|   READER	|     --   	|    M-M    |    O-M  	|
|   BOOK	|    M-M    |     --	|    O-M  	|
|   REVIEWS	|    O-M  	|    O-M  	|     --  	|

**BOOK**
|   ID	|   isbn	|   title	|   author	|   year	|

**READER**
|   ID	|   email	|   first_name	|   last_name	|   password_hash	|

**REVIEWS**
|   ID	|   review_date	|   rating	|   review_title	|   review_text	|   book_isbn fk	|   reader_id fk	|

**ASSOCIATION**
|   reader_id fk	|   book_isbn fk	|

# Packages Used
See requirements.txt

# Other Notes
My search feature started acting strange last minute after I did some refactoring. It worked before but now it seems to 
split the search term in to characters and finds all matching results.

I did get time to refactor the search commands to core SQL. Implementing the app with SQLAlchemy allowed me to work faster
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
