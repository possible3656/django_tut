from django.http import HttpResponse
#go to urls.py
#make a url then make a view for it 
# below two are view which are returning simple text
def about(request):
    return HttpResponse('about page')
    
def home(request):
    return HttpResponse('home page')