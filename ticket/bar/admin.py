from django.contrib import admin
from bar.models import Bar,BarThread,BarContributer

# Register your models here.
admin.site.register(Bar)
admin.site.register(BarThread)
admin.site.register(BarContributer)
