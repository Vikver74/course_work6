# Generated by Django 3.2.6 on 2022-11-02 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['-created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AddField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(max_length=2000, null=True, verbose_name='Текст объявления'),
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.ad', verbose_name='Объявление'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=2000, null=True, verbose_name='Текст объявления'),
        ),
    ]
