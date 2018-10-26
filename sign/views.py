from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# def index(request):
#     return HttpResponse("Hello Django!")    # 通过HttpResponse类向浏览器返回字符串

def index(request):
    return render(request, "index.html")    # 通过render函数向request请求返回HTML页面


# 登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # # HttpResponseRedirect类可以对路径进行重定向，从而将登录成功后的请求指向/event_manage/目录
            # return HttpResponseRedirect('/event_manage/')

            auth.login(request, user)
            # # 添加浏览器cookie
            # response.set_cookie('user', username, 3600)
            # 将session信息写入到浏览器
            request.session['user'] = username
            # 重定向路径
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


# 发布会管理
@login_required     # 该装饰器限制必须登录才能访问下面的页面
def event_manage(request):
    # # 读取浏览器cookie
    # username = request.COOKIES.get('user', '')
    # 读取浏览器session
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {"user": username})
