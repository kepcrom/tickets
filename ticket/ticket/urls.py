"""ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,path,include
from member import views as member_views
from rest_framework import routers
from ticket import views

router = routers.DefaultRouter(r'^api')
router.register(r':users',views.UserViewSet)
router.register(r':groups',views.GroupViewSet)
router.register(r':bar',views.BarViewSet)
router.register(r':member', views.MemberViewSet)

urlpatterns = [
    re_path(r'^$', member_views.index,name='index'),
    path('admin/', admin.site.urls),
    path('bar/', include('bar.urls')),
    path('member/', include('member.urls')),
    path('logout/', member_views.member_logout, name='logout'),
    re_path(r'^api', include(router.urls)),
    re_path(r'^api-auth', include('rest_framework.urls')),
]
