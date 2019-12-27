from django.shortcuts import render
from user.models import User
from django.http import HttpResponse, JsonResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt
import uuid


# Create your views here.
def selectUser(request):
    userList = User.objects.all()
    for i in range(0, userList.count()):
        print(userList[i].username)
    return HttpResponse(userList[0].username)


@csrf_exempt
def register(request):
    try:
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        email = request.POST.get("email")
        md5 = hashlib.md5()
        md5.update(pwd.encode("utf-8"))
        password = md5.hexdigest()
        user = User()
        id = str(uuid.uuid1())
        user.uid = id
        user.username = username
        user.password = password
        user.email = email
        user.save()
    except Exception as e:
        return JsonResponse({'code': '500', 'data': '', 'msg': str(e)})
    return JsonResponse({'code': '200', 'data': '', 'msg': 'success'})


@csrf_exempt
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist as e:
        print(str(e))
        return JsonResponse({'code': '401', 'data': '', 'msg': '此用户不存在！'})
    except User.MultipleObjectsReturned as e:
        print(str(e))
        return JsonResponse({'code': '500', 'data': '', 'msg': str(e)})

    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    password = md5.hexdigest()
    if password == user.password:
        return JsonResponse({"code": "200", "data": "", "msg": ""})
    else:
        return JsonResponse({"code": "402", "data": "", "msg": "密码不正确！"})
