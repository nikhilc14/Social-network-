# Generated by Django 3.2.5 on 2022-02-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_posts_unliked'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='icon_clicked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
