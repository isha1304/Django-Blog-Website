# Generated by Django 4.2.4 on 2023-09-13 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Myapp", "0006_alter_post_created_at_alter_post_upload_to"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Post",
        ),
    ]