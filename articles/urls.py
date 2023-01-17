
from django.urls import path
from . import view
# . means look in same directory as current file 
# we are importing view to get all the function from it 

urlpatterns = [
# we only need home here because we have created this app for homepage 
    path('',view.home),
]
