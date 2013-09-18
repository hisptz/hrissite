HRIS Site
==========
Human Resource Information System Site, is a python powered django-cms website,
aimed at publishing information related to development, implementation, training,
rollout and customization of Human Resource For Health Information system.

HRIS is an open source Human Resource Information system, currently ported to
symfony, it's being developed and maintained by the university of Dar es salaam.

How to Install and deploy this site.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Install virtualenv on your machine and use it to maintain the site.
The following are couple of commands for operating under virtual env:

	#Install python virtualenv
	$ sudo apt-get install python-virtualenv
	
	#Create a virtual environment directory
	$ virtualenv /path/to/virtualenv_dir
	
	#Activating virtual environment(while you're in virtualenv_dir)
	$ source bin/activate
	
	#Deactivating virtual env
	$ deactivate

After creating and activating virtualenv, while inside virtualenv folder,
clone this site's source codes:
	
	$ git clone https://github.com/chingalo/hrissite.git

Inside hrissite directory, install project dependencies inside: deps.txt
	
	$ cd hrissite
	$ pip install -r deps.txt

Add database and email configurations inside hrissite/settings.py, your
database configurations should look something similar to this:
	
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'HOST': 'localhost',
			'NAME': 'DATABASENAME',
			'USER': 'USERNAME',
			'PASSWORD': 'THESECRETPASSWORD',
		}
	}
	# EMAIL Server configurations
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_IMAP_HOST = 'imap.gmail.com'
	EMAIL_PORT = "587"
	EMAIL_HOST_USER = 'companyname@gmail.com'
	EMAIL_HOST_PASSWORD = 'companypassword'
	EMAIL_USE_TLS = True
	EMAIL_SENDER = 'companyname@gmail.com'
	EMAIL_SSL = True
Initial dummy database settings are stored under data branch.
After configuration sync database( run command: python manage.py syncdb --all) and then run the server. Incase of any difficulties
in configuration refer to [Django CMS Documentation](http://django-cms.readthedocs.org/en/2.2/getting_started/installation.html)
for more information.
