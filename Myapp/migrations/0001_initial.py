# Generated by Django 4.2.4 on 2023-09-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blogging",
            fields=[
                ("blog_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=1000)),
                ("content", models.TextField(blank=True, max_length=250, null=True)),
                ("image", models.ImageField(upload_to="blog")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("upload_to", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
