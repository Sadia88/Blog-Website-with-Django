# Generated by Django 4.1.6 on 2023-02-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
