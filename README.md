# ocljobs
A basic Django application and web front-end for accessing the GitHub Jobs API.

## To install:
Make sure you have python 2 or 3 installed on your system. I am pretty sure what I wrote is usable with both.

Then install Django 1.7.8 (probably works with 1.8 as well, didn't test)
`pip install django==1.7.8`

## To run:

To get the ocljobs source code, ensure you have SSH access to GitHub, then run:

	`$ git clone git@github.com:Cojomax99/ocljobs.git`

Change to the directory with manage.py in it

	`$ cd ocljobs`

These two commands will take care of setting up the database:
	`$ python manage.py migrate`
	`$ python manage.py makemigrations`
	
NOTE: I added use of an SQLite database so that results for each query are cached. It's not super intelligent caching, but if you use the same search terms it will use the cached results instead of hitting GitHub's database. This allows the application to be used offline, in some sense. It also allowed me to make a lot of test changes without constantly hitting GitHub's database!

To start a test server on http://localhost:8000:
	`$ python manage.py runserver`

To create a test superuser:
	`$ python manage.py createsuperuser`

For more information on Django’s management script, run python manage.py --help or consult Django’s excellent documentation at https://docs.djangoproject.com/en/1.8/.

To access the admin panel, go to `http://localhost:8000/admin`, and there you can see the entries and queries.
