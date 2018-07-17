# Rapid-fire Django/Bootstrap 4 Starter Template
----

A minimalist mobile-responsive template for starting a Django/Bootstrap project, utilizing Django 2.0 Bootstrap 4, jQuery, a base template and basic navigation, a sticky header and a footer.

### Usage:

1. Create a virtualenv: `python -m virtualenv my_venv_name`
2. `cd my_venv_name`
3. Activate it: `source bin/activate` (POSIX), `.\Scripts\activate`
4. `mkdir src` and clone this repo into it
5. `cd src`
6. `pip install -r requirements.txt` (may require `sudo`)

### Config:

If you are ok with using `my_project` and `my_app` for your project and app name respectively, you don't have to do anything at all. Just start the server and have fun! If you want to change your project/app names:

1. **my_project/settings.py**: Update `SECRET_KEY`, `INSTALLED_APPS`, `ROOT_URLCONF`, and `WSGI_APPLICATION` (see comments in file)
2. **my_project/wsgi.py**: Update project settings (see comments in file)
3. **src/manage.py**: Update project settings (see comments in file)
4. **my_app/apps.py**: Update app config (see comments in file)
5. *Optional: change comments (urls.py, manage.py, etc) to match your new project/app name*
6. Rename my_project and my_app folders to your new project and app names (these **must** match the updates you made above!)

### Start the server!

1. `python manage.py runserver`
2. Navigate to http://127.0.0.1:8000
3. Hooray! You've got a project, an app, and a base template to work with


