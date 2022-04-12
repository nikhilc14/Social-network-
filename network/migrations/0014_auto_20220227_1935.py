# Generated by Django 3.2.5 on 2022-02-27 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_user_post_clicked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='icon_clicked',
        ),
        migrations.RemoveField(
            model_name='user',
            name='post_clicked',
        ),
        migrations.CreateModel(
            name='click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_clicked', models.BooleanField(blank=True, default=False, null=True)),
                ('post_clicked', models.ManyToManyField(blank=True, related_name='likes_of_post', to='network.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
