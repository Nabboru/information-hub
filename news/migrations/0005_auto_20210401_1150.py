# Generated by Django 3.1.7 on 2021-04-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210330_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
