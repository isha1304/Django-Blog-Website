# Generated by Django 4.2.4 on 2023-10-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Myapp", "0036_post_header_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(default="home", max_length=255),
        ),
    ]