# Generated by Django 4.2.4 on 2023-09-22 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0022_alter_user_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]