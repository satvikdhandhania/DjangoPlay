## Commands 
# Practical Project using tutorial from W3Schools
https://www.w3schools.com/django/index.php 

# init python virtual environment 
```
python3 -m venv venv/
```

# activate virtual environment 
```
source venv/bin/activate
```

# install requirements 
``` 
pip3 install -r requirements.txt
```

# Update requirements file with installed packages
``` 
pip3 freeze > requirements.txt
```

# deactivate virtual environment 
```
deactivate
```

# Create a new Django project
```
django-admin startproject <project_name>
```

# Create a new Django app
```
python manage.py startapp <app_name>
```

# Create models and run migrations for app to use db.sqlite3
```
python manage.py makemigrations members

Sample output:
Migrations for 'members':
  members/migrations/0001_initial.py
    - Create model Member
```
The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder.
# Run migrate to build the custom app to be used in the my_tennis project root
```
python manage.py migrate 
```

# Run the Django development server
```
python manage.py runserver 
```

# View SQL
As a side-note: you can view the SQL statement that were executed from the migration above. All you have to do is to run this command, with the migration number:
```
python manage.py sqlmigrate members 0001
```
To open a Python shell, type this command:
```
python manage.py shell

Add Multiple Records

You can add multiple records by making a list of Member objects, and execute .save() on each entry:
>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
...   x.save()
...
>>>


Now, if you run this command:
>>> Member.objects.all().values()

you will see that there are 6 members in the Member table:
<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'},
{'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>

```

# Query Set
https://www.w3schools.com/django/django_queryset.php

# To update a record in the database, you can use the method:
```
>>> from members.models import Member
>>> x = Member.objects.all()[4] 
>>> x.firstname 
This should give you this result:
'Stale'
>>> x.firstname = 'Jane'
>>> x.save()
>>> Member.objects.all().values() 
 <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Jane', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'},
{'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]> 
```

# To delete a record in the database, you can use the method:
```
>>> from members.models import Member
>>> x = Member.objects.all()[4]
>>> x.firstname
'Stalikken'
>>> x.delete()
The result will be:
(1, {'members.Member': 1})
Which tells us how many items were deleted, and from which Model.
>>> Member.objects.all().values()
```



Add Fields in the Model

To add a field to a table after it is created, open the models.py file, and make your changes:
```
my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True) 
  joined_date = models.DateField(null=True)

```
<span style="color: red;"> note id null=true is not provided 
It is impossible to add a non-nullable field 'joined_date' to member without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 2
</span>
  