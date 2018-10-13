from django.conf import settings
from django.db import models
from member.models import MemberProfile
# Create your models here.
class Bar(models.Model):
    Number = models.IntegerField()
    Summary = models.TextField(blank=False,default="Summary")
    Creator = models.OneToOneField(MemberProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.Summary

class BarThread(models.Model):
    Bar = models.OneToOneField(Bar,on_delete=models.CASCADE)
    Date = models.DateTimeField( auto_now=True )
    Text = models.TextField(blank=False)
    Creator = models.OneToOneField(MemberProfile,on_delete=models.CASCADE)

class BarContributer(models.Model):
    Bar = models.ForeignKey(Bar,on_delete=models.CASCADE)
    Member = models.ForeignKey(MemberProfile,on_delete=models.CASCADE)
