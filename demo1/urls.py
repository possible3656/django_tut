
from django.contrib import admin
from django.urls import path
from . import view
# . means look in same directory as current file 
# we are importing view to get all the function from it 

urlpatterns = [
    path('admin/', admin.site.urls),
    # we created a endpoint and assigned it a view 
    # when its called that view is returned
    path('about/',view.about),
    # empty string denotes homepage 
    path('',view.home),
]
