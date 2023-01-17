in this lecture we learn about what is app and why we use it 
app can be called module for example homepage , about us page

so we created an new app by using `python manage.py startapp $appname`

after this we create urls.py file for that app then we define url and view for it 
then we created template to return in html under views.py

IMPORTANT 
after creating app we need to register it under settings.py for root app 

`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
]
`
like this 

then we add this url to urls.py of root app 
then runserver