from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):  # 标题类
    name = models.CharField(max_length=50)


class Tag(models.Model):  # 标题类
    name = models.CharField(max_length=50)


class Post(models.Model):  # 正文类
    title = models.CharField(max_length=70)  # 标题
    excerpt = models.CharField(max_length=200, blank=True)  # 摘要
    body = models.TextField()  # 正文
    created_time = models.DateField()  # 创建时间
    changed_time = models.DateField()  # 修改时间
    tags = models.ManyToManyField(Tag, blank=True)  # 标签
    catrgory = models.ForeignKey(Category, on_delete=models.CASCADE)  # 标题
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者
