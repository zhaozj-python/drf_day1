from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# from rest_framework.response import Response
# from rest_framework.views import APIView
# Create your views here.
from text1.models import User


@method_decorator(csrf_exempt, name="dispatch")  # 为类视图免除csrf认证
class UserView(View):

    def get(self, request, *args, **kwargs):
        """
        提供查询单个用户以及  多个用户的接口
        :param request:  请求对象
        :param args:
        :param kwargs:
        :return: 返回查询结果
        """
        user_id = kwargs.get("id")
        # print(user_id)
        if user_id:
            user_val = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            print(user_val)
            if user_val:
                # 如果查询出用户的信息, 则返回到前端
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user_val
                })
        else:
            user_objects_all = User.objects.all().values("username", "password", "gender")
            if user_objects_all:
                return JsonResponse({
                    "status": 200,
                    "message:": "查询所有用户成功",
                    "results": list(user_objects_all)
                })

        return JsonResponse({
            "status": 400,
            "message": "查询用户失败",
        })


    def post(self, request, *args, **kwargs):
        # 新增单个用户
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 200,
                "message": "新增单个用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })

        except:
            return JsonResponse({
                "status": 400,
                "message": "新增失败",
            })

    def put(self, request, *args, **kwargs):
        print("put 修改")
        return HttpResponse("put OK")

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        if user_id:
            user_del = User.objects.get(id=user_id)
            user_del.delete()
            return JsonResponse({
                "status": 200,
                "message": "删除单个用户成功",
                "results": "删除用户id为"+user_id
            })
        else:
            return JsonResponse({
                "status": 400,
                "message": "删除失败",
            })


# class StudentAPIView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         print("DRF GET VIEW")
#         return Response("DRF GET OK")
#
#     def post(self, request, *args, **kwargs):
#         print("POST GET VIEW")
#         return Response("DRF POST OK")
