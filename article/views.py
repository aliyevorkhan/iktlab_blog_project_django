from django.shortcuts import redirect, render, HttpResponse, get_object_or_404, reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

def index(request):
    keyword = request.GET.get('keyword' or None)
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, 'index.html', {"articles": articles})        

    articles = Article.objects.all()
    context = {
        "articles":articles,
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

@login_required(login_url='user:login')
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles,
    }
    return render(request, "dashboard.html", context)

@login_required(login_url='user:login')
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
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

@login_required(login_url='user:login')
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Post Silindi")
    return redirect('article:dashboard')

def detail(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    context = {
        "article": article,
        "comments": comments,
    }
    return render(request, "detail.html", context)


@login_required(login_url='user:login')
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Post Redaktə Edildi")
        return redirect('article:dashboard')
    context={
        "form":form,
    }
    return render(request, 'edit.html', context)

@login_required(login_url='user:login')
def comment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        comment_author = request.user
        comment_content = request.POST.get('comment_content')
        comment = Comment(comment_author=comment_author, comment_content=comment_content)
        comment.article = article
        comment.save()
    messages.success(request, "Rey bildirildi")
    # return redirect("/articles/detail/{}".format(id))
    return redirect(reverse('article:detail', kwargs={'id':id}))