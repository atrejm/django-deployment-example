# Generated by Django 4.1 on 2023-02-20 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usermodel",
            name="junk",
        ),
    ]
