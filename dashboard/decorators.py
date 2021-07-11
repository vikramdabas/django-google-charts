from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func


def allowed_users(allowed_roles=()):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group_list = []
            has_access = False
            if request.user.groups.exists():
                groups = request.user.groups.all()
                for group in groups:
                    group_list.append(group.name)
                    if str(group.name) in allowed_roles:
                        has_access = True
            if 'Admin' in group_list:
                has_access = True
            if has_access:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('no_access')
        return wrapper_func
    return decorators


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group_list = []
        if request.user.groups.exists():
            groups = request.user.groups.all()
            for group in groups:
                group_list.append(group.name)
        if 'Admin' in group_list:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_access')
    return wrapper_func

