# Rapid-fire Django/Bootstrap 4 Starter Template

A minimalist mobile-responsive template for starting a Django/Bootstrap project, utilizing Django (latest), Bootstrap 4, jQuery, a base template and basic navigation, a sticky header and a footer. Using this template assumes you know how Django works, you've gotten sick of repetitively creating the core layout for Django projects and just want to rename a few things and get coding! There may be missing steps in this readme, but I've tried to make sure to cover everything. If it doesn't work perfectly, I trust that you'll be able to figure it out :) If not, submit a pull request and I'll fix it! Note that you may want to update CDN links to new versions of stuff as this repo ages.

### Includes setup for:

1. Django (latest)
2. Bootstrap 4.1.2 and its dependencies
3. jQuery 3.3.1
4. Basic template setup including base, home, about, contact, navigation/header and footer.

### Usage:

1. Create a virtualenv: `python -m virtualenv my_venv_name`
2. `cd my_venv_name`
3. Activate it: `source bin/activate` (POSIX), `.\Scripts\activate` (Windows)
4. `mkdir src`
5. `cd src` and and clone this repo into it (`git clone https://github.com/ckz8780/django_bs4_starter_template.git .`)
6. `pip install -r requirements.txt` (may require `sudo` opn POSIX systems)

### Config:

If you are ok with using `my_project` and `my_app` for your project and app name respectively, you don't have to do anything at all. Just start the server and have fun! If you want to change your project/app names:

1. **my_project/settings.py**: Update `SECRET_KEY`, `INSTALLED_APPS`, `ROOT_URLCONF`, and `WSGI_APPLICATION` (see comments in file)
2. **my_project/wsgi.py**: Update project settings (see comments in file)
3. **my_project/urls.py**: Update app urls include (see comments in file)
4. **src/manage.py**: Update project settings (see comments in file)
5. **my_app/apps.py**: Update app config (see comments in file)
6. *Completely Optional (for perfectionists): change comments (urls.py, manage.py, etc) to match your new project/app name*
7. Rename my_project and my_app folders to your new project and app names (these **must** match the updates you made above!)
8. Delete src/.git folder and re-initialize your own: `git init`

### Start the server!

1. `python manage.py runserver`
2. Navigate to http://127.0.0.1:8000
3. Hooray! You've got a project, an app, and a base template to work with. Change colors/nav links/app templates/whatever else as you see fit and have fun!
4. For production, configure static files/databases/secret keys/etc as you see fit


