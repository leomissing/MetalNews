# Generated by Django 3.1.5 on 2021-01-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Metal', '0005_auto_20210120_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_author',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_author',
            field=models.CharField(default='kek', max_length=200, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
