from django.http import HttpResponse, JsonResponse
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt
import functools
import re
# from . import cus_respone
from .cus_respone import CusHttpRespone
from .cus_error import *


# Create your views here.


def param_check(param, method='GET'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            # data = request.GET
            # if method == 'POST':
            #     data = request.POST
            # if param in data:
            #     pass
            # else:
            #     return Param_miss
            try:

                print(args)
                request = args[0]
                data = set(request.GET)
                in_param = set(param)
                print('1')
                if method == 'POST':
                    data = set(request.POST)

                print(set(param), data, in_param)
                if set(param) != data & in_param:
                    print('in')
                    return Param_miss
                return func(*args, **kw)
            except Exception as e:
                print('Error', e)

        return wrapper

    return decorator


def index(request):
    return HttpResponse('Django Project')  # 表现层，最终呈现的东西


def login(request):
    user_id = request.POST.get('user_id')
    password = request.POST.get('password')
    db_user_id = User.objects.filter(user_id=user_id).first()
    if db_user_id:
        db_password = db_user_id.password
        if password != db_password:
            return JsonResponse(password_error)
    else:
        return JsonResponse(No_user_id)



    pass


def login_out():
    pass


@param_check(param=['user_id', 'iphone', 'email', 'password'])
def add_data(request):
    # 获取数据
    try:
        username = request.GET.get('user_id')
        print(username)
        petname = request.GET.get('user_pet_name')
        iphone = request.GET.get('iphone')
        email = request.GET.get('email')
        password = request.GET.get('password')
        age = request.GET.get('age')
        address = request.GET.get('address')
        info = request.GET.get('info')

        if username:
            if username.isalnum():
                if len(username) <= 16:
                    pass
                else:
                    return User_name_long
            else:
                return user_id_error
        else:
            return enter_user_id

        if iphone:
            if iphone.isdigit():
                if len(iphone) == 11:
                    pass
                else:
                    return iphone_error
            else:
                return iphone_digit
        else:
            return iphone_null

        if email:
            if len(email) > 7:
                if re.match(r'^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+)$'):
                    pass
            else:
                return email_error
        else:
            return email_null

        if password.isalum():
            if 8 < len(password) < 16 :
                pass
            else:
                return password__inv
        else:
            return password_inv_str
        # 保存数据
        User.objects.create(user_id=username, user_pet_name=petname, iphone=iphone, email=email, password=password,
                            age=age, address=address, info=info)
        # result = {'user_id': username, 'user_pet_name': petname, 'iphone': iphone, 'email': email, 'password': password,
        #           'age': age, 'address': address, 'info': info}
        result = {'code': 200, 'msg': '成功'}
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        print(e)


@param_check(param=['id'])
def delete_data(request):
    user_ids = request.GET.get('id')
    ft = User.objects.filter(id=user_ids).first()  # 过滤验证
    if ft:
        ft.delete()
    return HttpResponse('delete successful')


@param_check(param=['user_id', 'password', ], method='POST', )
@csrf_exempt
def updata(request):
    username = request.POST.get('user_id')
    petname = request.POST.get('user_pet_name')
    iphone = request.POST.get('iphone')
    email = request.POST.get('email')
    password = request.POST.get('password')
    age = request.POST.get('age')
    address = request.POST.get('address')
    info = request.POST.get('info')
    ids = request.POST.get('id')
    # print(ids)
    # # print(request.POST)
    # # User.objects.filter(id=int(ids)).update(**request.POST)
    User.objects.filter(id=ids).update(user_id=username, user_pet_name=petname, iphone=iphone, email=email,
                                       password=password, age=age, address=address, info=info)
    return HttpResponse('Data updated')


@param_check(param=['id'])
def search_data(request):
    user_id = request.GET.get('id')
    if user_id:
        user = User.objects.filter(id=user_id).first()
        print(user)
        result = user.to_dict()
        # return HttpResponse(result, cus_respone)
        # return HttpResponse(result)
        print(result)
        return CusHttpRespone(result)
        # return JsonResponse(result)
    else:
        return HttpResponse('Please enter id')
