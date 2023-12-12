from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

class Register(TemplateView):
    template_name = "register/register.html"

    def post(self, request, *args, **kwargs):
        data = dict(request.POST.items())
        name = data['name']
        email = data['email']
        password = data['password']
        re_passwor = data['repeat_password']

        user = User.objects.create(
            username = email,
            first_name = name,
            email = email,
        )
        user.set_password(password)
        user.save()

        login(request, user)
        return redirect('index')


class Login(TemplateView):
    template_name = "register/login.html"

    def post(self, request, *args, **kwargs):
        data = dict(request.POST.items())
        email = data['email']
        password = data['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("email or password incorrect!")

def logout_veiw(request):
    logout(request)
    return redirect('index')
