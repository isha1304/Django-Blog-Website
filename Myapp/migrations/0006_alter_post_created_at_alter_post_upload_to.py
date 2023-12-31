# Generated by Django 4.2.4 on 2023-09-13 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Myapp", "0005_post_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="post",
            name="upload_to",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
