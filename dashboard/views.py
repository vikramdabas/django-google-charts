from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DataCount, DataSerializer
from .models import DashboardConfig
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user, allowed_users, admin_only


class Dashboard(View):
    @method_decorator(allowed_users(allowed_roles=['TEAM_A']))
    def get(self, request):
        if request.user.is_authenticated:
            dashboard_config = DashboardConfig.objects.filter().values()
            return render(request, 'dashboard.html',
                          {"username": request.user,
                           "dashboard_config": dashboard_config
                           })
        else:
            return HttpResponseRedirect("/")


class Unauthorized(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'unauthorized.html',
                          {"username": request.user, "userlogin": request.user.last_login})
        else:
            return HttpResponseRedirect("/")


@api_view(['GET'])
def data_detail(request):
    if request.method == 'GET':
        data = DataCount.objects.filter().order_by('id')
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)
