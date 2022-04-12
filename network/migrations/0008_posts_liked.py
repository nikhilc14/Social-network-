# Generated by Django 3.2.5 on 2022-02-23 07:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_alter_posts_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]