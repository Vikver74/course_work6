# Generated by Django 3.2.6 on 2022-11-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]