from django.http import HttpResponse
#go to urls.py
#make a url then make a view for it 
# below two are view which are returning simple text
from django.shortcuts import render

def about(request):
   # return HttpResponse('about page')
   return render(request,'about.html')
    
def home(request):
   # return HttpResponse('home page')
   return render(request,'homepage.html')