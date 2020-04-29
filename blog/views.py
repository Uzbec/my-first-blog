from django.shortcuts import render


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
