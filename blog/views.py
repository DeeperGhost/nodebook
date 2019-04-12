from django.shortcuts import render
from notebook import NODEBOOK
# from django.views.generic import TemplateView

from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
# def post_list(request):
#     return render(request, 'blog/index.html', {})

class listView(View):
    nodebook  = NODEBOOK()

    def get(self, request, *args, **kwargs):
        dbstr = self.nodebook.PRINT_NODES(nameList='dataProductBase')
        dbTaskList = self.nodebook.PRINT_NODES(nameList='TaskList')
        #     keys = dbstr.keys()
        # return HttpResponse('Hello, World!')
        return render(request, 'blog/index.html', {'data': dbstr.items(),'dataTaskList': dbTaskList.items()})




def login(request):

    return render(request, 'blog/login.html', {})

# def index(request):
#     nodebook  = NODEBOOK()
#     dbstr = nodebook.PRINT_NODES()
#     keys = dbstr.keys()
#     # for key in keys:
#     #     dbstr[key]
#
#
#     t = 5+2
#     # return render(request, 'blog/index.html', {'dbstr':dbstr, 'keys':keys})
#     return render(request, 'blog/index.html', {'data': dbstr.items()})

def base(request):
    return render(request, 'blog/base.html', {})

def list(request):
    return render(request, 'blog/list.html', {})

def statistic(request):
    return render(request, 'blog/statistic.html', {})

# class index(TemplateView):
#     template_name = "blog/index.html"