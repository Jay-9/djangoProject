from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        # 处理POST请求的逻辑
        # 获取到用户提交的用户名和密码
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 进行校验；校验成功告知登录成功
        if user == 'jay' and pwd == '1':
            # return HttpResponse('登录成功')
            return redirect('/index/')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
