from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
def view_articles(request):
    articles = Article.objects.all()
    return render(request,"articles/articles.html",context={"articles":articles})    
def view_article(request,slug):
    return HttpResponse("Page d'article")
