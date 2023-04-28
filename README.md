# CRUD_01
Django Function-Based CRUD Example
This is an example Django application that demonstrates how to implement CRUD operations using function-based views. It uses Django's built-in ListView, CreateView, UpdateView, and DeleteView classes to handle the HTTP methods.

Getting Started
To run this application, you will need Python 3 and Django 3 installed on your machine.

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/django-function-based-crud-example.git
Change into the project directory:
bash
Copy code
cd django-function-based-crud-example
Create a virtual environment:
bash
Copy code
python3 -m venv env
Activate the virtual environment:
bash
Copy code
source env/bin/activate
Install the dependencies:
Copy code
pip install -r requirements.txt
Apply the migrations:
Copy code
python manage.py migrate
Run the server:
Copy code
python manage.py runserver
The application will be available at http://localhost:8000/.

Usage
The application has a simple model called Book with fields for title, author, and description.

List View
The list view displays a list of all books in the database. It is implemented using Django's ListView class.

URL: /books/

Create View
The create view displays a form for creating a new book. It is implemented using Django's CreateView class.

URL: /books/create/

Update View
The update view displays a form for updating an existing book. It is implemented using Django's UpdateView class.

URL: /books/update/<pk>/

Delete View
The delete view displays a confirmation form for deleting an existing book. It is implemented using Django's DeleteView class.

URL: /books/delete/<pk>/

URLs and Views
The URLs and views are defined in the urls.py and views.py files, respectively.

Contributing
If you would like to contribute to this project, please open a pull request with your changes.





