# Generated by Django 4.2.4 on 2023-10-20 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Myapp", "0040_profile_bio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="header_image",
        ),
    ]