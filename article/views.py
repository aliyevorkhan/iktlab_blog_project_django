from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("ESAS SEHIFE")
    return render(request, "article/index.html")