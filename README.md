Installation Steps
1. Set up a Virtual Environment
Open your terminal and navigate to your desired project folder:

cd /path/to/your/projects
Create a virtual environment:

python -m venv env
Activate the virtual environment:

On Windows:

env\Scripts\activate
On macOS/Linux:

source env/bin/activate
Install Django:


pip install django






2. Create a Django Project
Start a new Django project:


django-admin startproject myproject
Navigate into the project directory:


cd myproject






3. Add Your App
Create a new Django app named myapp:


python manage.py startapp myapp
Add myapp to the INSTALLED_APPS list in myproject/settings.py:

python
Copy code
INSTALLED_APPS = [
    ...
    'myapp',
]



4. Set Up the Model
In myapp/models.py, define the Invoice model:

python
Copy code
from django.db import models

class Invoice(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    summary = models.TextField()



    
Apply the model to the database:

python manage.py makemigrations
python manage.py migrate






5. Register the Model in Admin
In myapp/admin.py, register the Invoice model:

python
Copy code
from django.contrib import admin
from .models import Invoice

admin.site.register(Invoice)
Run the server:

bash
Copy code
python manage.py runserver
Visit the admin panel at http://127.0.0.1:8000/admin/, log in (create a superuser if needed), and see the Invoice model.





6. Create Views and Templates
Define views in myapp/views.py:

python
Copy code
from django.shortcuts import render
from .models import Invoice

def accept(request):
    if request.method == 'POST':
        Invoice.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            email=request.POST['email'],
            product=request.POST['product'],
            price=request.POST['price'],
            summary=request.POST['summary']
        )
    return render(request, 'accept.html')

def list(request):
    item = Invoice.objects.all()
    return render(request, 'list.html', {'item': item})
Add URLs in myproject/urls.py:

python
Copy code
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", views.list, name='list'),
    path("acc/", views.accept, name='accept'),
]
Create templates in myapp/templates/:

accept.html:

html
Copy code
<!DOCTYPE html>
<html>
<body>
    <form method="POST">
        {% csrf_token %}
        <label>Name:</label> <input type="text" name="name"><br>
        <label>Phone:</label> <input type="text" name="phone"><br>
        <label>Address:</label> <input type="text" name="address"><br>
        <label>Email:</label> <input type="text" name="email"><br>
        <label>Product:</label> <input type="text" name="product"><br>
        <label>Price:</label> <input type="text" name="price"><br>
        <label>Summary:</label> <textarea name="summary"></textarea><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
list.html:

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        .item { border: 1px solid #ccc; margin: 10px; padding: 10px; }
    </style>
</head>
<body>
    {% for i in item %}
    <div class="item">
        <h2>{{ i.name }}</h2>
        <p><strong>Phone:</strong> {{ i.phone }}</p>
        <p><strong>Email:</strong> {{ i.email }}</p>
        <p><strong>Address:</strong> {{ i.address }}</p>
        <p><strong>Product:</strong> {{ i.product }}</p>
        <p><strong>Price:</strong> ${{ i.price }}</p>
        <p><strong>Summary:</strong> {{ i.summary }}</p>
    </div>
    {% endfor %}
</body>
</html>




7. Run the Application
Start the development server:

bash
Copy code
python manage.py runserver
Open your browser:

Visit http://127.0.0.1:8000/acc/ to add invoices.
Visit http://127.0.0.1:8000/list/ to view all invoices.
