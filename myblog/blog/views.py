from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from . import models
# Create your views here.

def index(request):
    articles=models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def add_page(request):
    if request.method == 'GET':
        return render(request,'blog/add_page.html')
    else:
        title=request.POST.get("title")
        content=request.POST.get("content")
        models.Article.objects.create(title=title,content=content)
        return redirect('/blog/index/')
def article_page(request,article_id):
    article=models.Article.objects.filter(id=article_id).first()
    return render(request,'blog/article_page.html',{"article":article})

def edit_page(request,article_id):
    article = models.Article.objects.filter(id=article_id).first()
    return render(request, 'blog/edit_page.html', {"article": article})


def edit_action(request,article_id):
    title = request.POST.get("title")
    content = request.POST.get("content")
    models.Article.objects.filter(id=article_id).update(title=title, content=content)
    return redirect('/blog/index/')

