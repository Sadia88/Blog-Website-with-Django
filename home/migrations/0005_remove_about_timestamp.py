# Generated by Django 4.1.6 on 2023-02-02 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_about_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='timeStamp',
        ),
    ]