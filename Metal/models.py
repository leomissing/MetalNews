from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Post(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    author = models.CharField(max_length=200, verbose_name='Автор')
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержание')
    data = models.DateTimeField(auto_now=True, verbose_name='Дата')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    post_likes = models.IntegerField(default=0, verbose_name='Лайки')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        ordering = ['-data']


class Comments(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    comment_text = models.TextField(verbose_name='Комментарий')
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=200, verbose_name='Автор')
    data = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __str__(self):
        return self.comment_text

    class Meta:
        db_table = 'comments'
        ordering = ['-data']
