# Generated by Django 3.2 on 2021-04-16 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_rename_blogs_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='creat_time',
            new_name='created_time',
        ),
    ]
