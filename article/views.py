from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

def index(request):
    context = {
        "age": 20,
        "numbers": [1,2,3,4]
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def detail(request, id):
    return HttpResponse("Detail: {}".format(id))

def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles,
    }
    return render(request, "dashboard.html", context)

def add_article(request):
    form = ArticleForm(request.POST or None)
    context={
        "form":form,
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Post Əlavə Edildi")
        return redirect('article:dashboard')
    
    return render(request, "add_article.html", context)

def delete(request, id):
    article = Article.objects.filter(id=id)
    article.delete()
    return redirect('article:dashboard')

def detail(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    context = {
        "article": article,
    }
    return render(request, "detail.html", context)


def edit(request, id):
    return redirect('article:dashboard')
