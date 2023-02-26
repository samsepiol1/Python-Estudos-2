from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    resumo = models.CharField(max_length=255)
    content = models.CharField()
    autor = models.ForeignKey(User,on_delete=models.PROTECT)
    creat_at = models.DataField(auto_now_add = True)


