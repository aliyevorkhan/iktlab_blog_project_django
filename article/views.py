from django.shortcuts import render, HttpResponse

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