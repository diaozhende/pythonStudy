# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from book.models import BookModel, BookRole
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    return HttpResponse("<h1>hello world,You're at the polls index.</h1>")


def index_html(request):
    bookList = BookModel.objects.all()
    template = loader.get_template('book/index.html')
    context = RequestContext(request, {'bookList': bookList})
    context.push(locals())
    res = template.render(context=locals(), request=request)
    return HttpResponse(res)


def index_template(request):
    bookList = BookModel.objects.all()
    return render(request, 'book/index.html', {'bookList': bookList})


def book_home(request):
    book = BookModel.objects.all()
    return render(request, 'book/book_home.html', {'bookList': book})


def bookRoleInfo(request, id):
    print(id)
    book = BookModel.objects.get(id=id)
    bookRole = book.bookrole_set.all()
    return render(request, 'book/bookRoleInfo.html', {'bookRole': bookRole})


def toBookGetTest(request):
    return render(request, 'book/get.html', {})


def bookGetTest(request):
    print(request.GET.get("a"))
    print(request.GET.get("b"))
    print(request.GET.get("c"))
    print(request.GET.get("d"))
    return JsonResponse({'code': '200', 'data': '', 'msg': 'success'})


@csrf_exempt
def bookPostTest(request):
    try:
        print(request.POST.get("a"))
        print(request.POST.get("b"))
        print(request.POST.get("c"))
        print(request.POST.get("d"))
    except:
        return HttpResponse("{'code': '500', 'data': '', 'msg': 'error'}")
    return HttpResponse("{'code': '200', 'data': '', 'msg': 'success'}")
