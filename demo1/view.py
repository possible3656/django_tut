from django.http import HttpResponse
def about(request):
    return HttpResponse('about page')
    
def home(request):
    return HttpResponse('home page')