from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def index(request):
    return render(request, 'blog/index.html')


def login(request):
    return render(request, "blog/login.html")


def add_adward(request):
    return render(request, "blog/add_adward.html")


def group(request):
    return render(request, "blog/group.html")


def registration(request):
    return render(request, "blog/registration.html")


def user_page(request):
    return render(request, "blog/user_page.html")


def user_page_editor(request):
    return render(request, "blog/user_page_editor.html")


def asd(request):
    return render(request, "blog/asd.html")


def result_search(request):
    return render(request, "blog/result_search.html")


def registration(request):
    return render(request, "registration.html")


def reg_user(request):
    if request.method == "POST":
        loginName = request.POST.get("loginN")
        email = request.POST.get("email")
        password = request.POST.get("password")
        firstName = request.POST.get("first_name")
        lastName = request.POST.get("last_name")
        # Создайте пользователя и сохраните его в базе данных
        user = User.objects.create_user(username=loginName, email=email,
                                        password=password)
        # Обновите поля и сохраните их снова
        user.first_name = firstName
        user.last_name = lastName
        user.save()
    return HttpResponseRedirect("/accounts/login/")
