# Generated by Django 3.2.5 on 2022-02-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post',
            field=models.TextField(null=True),
        ),
    ]
