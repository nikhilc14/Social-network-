# Generated by Django 3.2.5 on 2022-02-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20220227_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='post_clicked',
            field=models.ManyToManyField(blank=True, related_name='likes_of_post', to='network.posts'),
        ),
    ]
