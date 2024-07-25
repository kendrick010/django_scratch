create project
```
cd src
django-admin startproject <PROJECT_NAME> .
```

start server
```
python3 manage.py runserver
```

create super user
```
python3 manage.py createsuperuser
```

create app
```
python3 manage.py startapp <APP_NAME>
```

apply migrations (whenever changes to model)
```
python3 manage.py makemigrations
python3 manage.py migrate
```

populate db using ORM
```python
python3 manage.py shell 

from products.models import Product
obj = Product.objects.get(id=1)   # gets object by primary key
```
