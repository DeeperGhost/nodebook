from django.shortcuts import render

# Create your views here.
# def post_list(request):
#     return render(request, 'blog/index.html', {})

def login(request):
        return render(request, 'blog/login.html', {})

def index(request):
    return render(request, 'blog/index.html', {})

def base(request):
    return render(request, 'blog/base.html', {})

def list(request):
    return render(request, 'blog/list.html', {})

def statistic(request):
    return render(request, 'blog/statistic.html', {})