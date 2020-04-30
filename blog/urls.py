from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('group', views.group, name="group"),
    path('add_adward', views.add_adward, name="add_adward"),
    path('registration', views.registration, name="registration"),
    path('user_page', views.user_page, name="user_page"),
    path('user_page_editor', views.user_page_editor, name="user_page_editor"),
    path('result_search', views.result_search, name='result_search'),
    path('asd', views.asd, name='asd'),


]