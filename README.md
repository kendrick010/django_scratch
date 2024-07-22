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