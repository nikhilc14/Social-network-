# Generated by Django 3.2.5 on 2022-02-18 05:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 2, 18, 5, 10, 4, 864143, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
