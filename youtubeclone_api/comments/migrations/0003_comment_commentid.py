# Generated by Django 3.1.8 on 2021-06-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20210528_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
