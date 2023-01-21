from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse

# Create your views here.


def home(request):
    # articles = Articles.objects.all()
    # articles = Articles.objects.all().values()
    articles = Articles.objects.a
    context = {
        articles: articles
    }
    return render(request, 'articles/home.html', context=context)
    # return HttpResponse(articles)
