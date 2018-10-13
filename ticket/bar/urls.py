from django.urls import path, re_path
from bar import views

app_name="bar"

urlpatterns = [
    path('create/',views.create, name="create"),
    path('save/',views.save, name="save"),
]
