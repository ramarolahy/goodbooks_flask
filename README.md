# Project 1
+ By: Mbinintsoa 'Ram' Ramarolahy
+ Production URL: <url>


# Website description


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

# Website requirements
+ **Registration**: Users should be able to register for your website, providing (at minimum) a username and password.
+ **Login**: Users, once registered, should be able to log in to your website with their username and password.
+ **Logout**: Logged in users should be able to log out of the site.
+ **Import**: Provided for you in this project is a file called ```books.csv```, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN nubmer, a title, an author, and a publication year. In a Python file called ```import.py``` separate from your web application, write a program that will take the books and import them into your PostgreSQL database. You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another. Run this program by running ```python3 import.py``` to import the books into your database, and submit this program with the rest of your project code.
+ **Search**: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!
+ **Book Page**: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.
+ **Review Submission**: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.
+ **Goodreads Review Data**: On your book page, you should also display (if available) the average rating and number of ratings the work has received from Goodreads.
+ **API Access**: If users make a GET request to your website’s ```/api/<isbn>``` route, where ```<isbn>``` is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON should follow the format:
```json
{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}
```

If the requested ISBN number isn’t in your database, your website should return a 404 error.

+ You should be using raw SQL commands (as via SQLAlchemy’s ```execute``` method) in order to make database queries. You should not use the SQLAlchemy ORM (if familiar with it) for this project.
+ In ```README.md```, include a short writeup describing your project, what’s contained in each file, a list of all of the tables in your database and what column names (and data types) are in each column, and (optionally) any other additional information the staff should know about your project.
If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to ```requirements.txt```!
Beyond these requirements, the design, look, and feel of the website are up to you! You’re also welcome to add additional features to your website, so long as you meet the requirements laid out in the above specification!

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
User1
    email: user1@test.com
    pw: pass1
User2
    email: user2@test.com
    pw: pass2
