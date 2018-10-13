from django.urls import path, re_path
from member import views

app_name = 'member'

urlpatterns = [
    path( 'register/', views.member_register, name="register"),
    path( 'member_login', views.member_login, name="member_login")
]
