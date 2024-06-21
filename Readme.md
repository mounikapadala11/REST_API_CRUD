# Flask CRUD REST API Example

This project demonstrates how to create a simple CRUD (Create, Read, Update, Delete) REST API using Python and Flask. The API manages a list of books, allowing you to perform CRUD operations on them.

## Prerequisites
Python 3.x
Flask
Installation

## Install Flask:

``` bash

pip install Flask
```

Project Setup: Create a directory and the following files within it:
``` bash
my_flask_app/
├── app.py
├── books.py
└── id_generator.py
```

## Code Explanation
** books.py **: This file contains the initial data structure for the books.

** id_generator.py **: This file contains the ID generation utility to ensure each new book gets a unique ID.

** app.py **: This file contains the main Flask application and defines the CRUD endpoints.

## Running the Application

The API will be running on http://127.0.0.1:5000.

API Endpoints -
Get all books:
``` bash
GET /books
```
Get a specific book:
``` bash
GET /books/<book_id>
```

Create a new book:
``` bash
POST /books
```
Request Body (JSON):
``` bash
{
  "title": "New Book Title",
  "author": "Author Name"
}
```

Update an existing book:
``` bash
PUT /books/<book_id>
```

Request Body (JSON):
```bash
{
  "title": "Updated Book Title",
  "author": "Updated Author Name"
}
```
Delete a book:
``` bash
DELETE /books/<book_id>
```

# Understanding the Code
## Flask Basics
Flask: A lightweight WSGI web application framework in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

Routes: Defined using the @app.route decorator, which maps a URL to a Python function.

HTTP Methods: Specify the HTTP methods (GET, POST, PUT, DELETE) that your endpoint responds to.

## Handling JSON
request.get_json(): Parses the incoming JSON request data.

jsonify(): Converts a Python dictionary to a JSON response.


## Global Variables
books: A list of dictionaries representing the books. This is a simple in-memory storage for demonstration purposes.

id_generator: An instance of the IDGenerator class to generate unique IDs for new books.

## Error Handling
404 Not Found: If a book with the specified ID does not exist, return a JSON response with an error message and a 404 status code.

## Running the Application
if __name__ == '__main__':: Ensures the app runs only if the script is executed directly, not if it is imported as a module.

## Conclusion
This example provides a basic understanding of how to create a REST API with Flask in Python, manage data with a simple in-memory structure, and handle CRUD operations. You can extend this example by integrating with a database, adding authentication, and more advanced features.