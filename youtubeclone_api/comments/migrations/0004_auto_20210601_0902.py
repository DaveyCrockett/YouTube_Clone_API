# Generated by Django 3.1.8 on 2021-06-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_comment_commentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentId',
            field=models.IntegerField(default=None),
        ),
    ]
