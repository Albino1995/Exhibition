from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from utils.LoginRequiredMixin import LoginRequiredMixin
from .forms import LoginForm, MessageForm
from .models import Message


class LoginView(View):
    """
    登录
    """
    @staticmethod
    def get(request):
        return render(request, 'login.html', {})

    @staticmethod
    def post(request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):
    """
    登出
    """
    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class MessageView(LoginRequiredMixin, View):
    """
    意见
    """
    @staticmethod
    def get(request):
        return render(request, 'suggestion.html', {'flag': 0})

    @staticmethod
    def post(request):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = Message()
            message.user = request.user
            message.mobile = request.POST.get('mobile', '')
            message.message = request.POST.get('message', '')
            message.save()
            return render(request, 'suggestion.html', {'flag': 1})
        else:
            return render(request, 'suggestion.html', {'message_form': message_form, 'flag': 0})


def page_not_fount(request):
    """
    404处理函数
    """
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

