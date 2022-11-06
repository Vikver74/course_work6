import datetime

from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', null=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True)
    description = models.TextField(max_length=2000, verbose_name='Текст объявления', null=True)
    author = models.ForeignKey(User, related_name='ads', verbose_name='Автор', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    image = models.ImageField(null=True)


    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Текст объявления', null=True)
    author = models.ForeignKey(User, related_name='comments', verbose_name='Автор', on_delete=models.CASCADE, default=1)
    ad = models.ForeignKey(Ad, related_name='comments', verbose_name='Объявление', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
