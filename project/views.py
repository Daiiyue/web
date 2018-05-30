from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from project.models import UserInfo, AreaInfo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def register_check(request):
    name = request.POST.get('username')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    # warn_data = 1
    try:
        UserInfo.objects.get(name=name)
        return HttpResponse('用户名重复')
        # return render(request, 'register.html', {'warn_data': warn_data})
    except:
        usr = UserInfo()
        usr.name = name
        usr.password = pwd
        usr.email = email
        usr.phone = phone
        usr.save()
        return render(request, 'register_check.html')


def login(request):
    if 'usr' in request.COOKIES:
        username = request.COOKIES['usr']
    else:
        username = ""
    return render(request, 'login.html', {'username': username})


def login_check(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    rem_name = request.POST.get('rem_name')
    try:
        usr = UserInfo.objects.get(name=username)
        if pwd == usr.password:
            response = redirect('/show_msg')
            request.session['usr'] = username
            # response.set_cookie('usr', username)
            # response = JsonResponse({'res': 1}) ajax
            if rem_name == 'on':
                # request.session['usr'] = username
                response.set_cookie('usr', username)
                # return render(request, 'login_check.html') 表单实现
            return response

        else:
            return redirect('/login')
            # return JsonResponse({'res': 2})
    except:
        # return HttpResponse('用户名或密码错误')
        return redirect('/login')


def show_msg(request):
    try:
        username = request.session.get('usr')
        # username = request.COOKIES['usr']
        UserMsg = UserInfo.objects.get(name=username)
        phone = UserMsg.phone
        email = UserMsg.email
        content = {'username': username, 'phone': phone, 'email': email}
        return render(request, 'show_msg.html', content)
    except:
        return redirect('/login')


def html_escape(request):
    context = {'content': '<h1>hello world</h1>'}
    return render(request, 'html_escape.html', context)


def zero_two(request):
    print(request.META['REMOTE_ADDR'])
    return render(request, '02.html')


def url_reverse(request):
    return render(request, 'url_reverse.html')


def show_args(request, a, b):
    return HttpResponse(a + ":" + b)


def show_kwargs(request, c, d):
    return HttpResponse(c + ":" + d)


from django.core.urlresolvers import reverse


def test_rediret(request):
    # return redirect('/02')
    url = reverse('booktest:show_kwargs', kwargs={'c': 3, 'd': 4})
    return redirect(url)


from django.core.paginator import Paginator


def area(request, pindex):
    list1 = AreaInfo.objects.filter(pid__isnull=True)
    p = Paginator(list1, 10)
    if pindex == '':
        pindex = '1'
    pindex = int(pindex)
    list2 = p.page(pindex)
    plist = p.page_range
    content = {'list': list2, 'plist': plist, 'pindex': pindex}
    return render(request, 'area.html', content)


def area1(request):
    return render(request, 'area1.html')


def area2(request):
    list = AreaInfo.objects.filter(pid__isnull=True)
    list2 = []
    for item in list:
        list2.append([item.id, item.atitle])
    return JsonResponse({'data': list2})


def area3(request, parent_id):
    list = AreaInfo.objects.filter(pid = parent_id)
    list2 = []
    for item in list:
        list2.append([item.id, item.atitle])
    return JsonResponse({'data': list2})
