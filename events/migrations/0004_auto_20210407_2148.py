# Generated by Django 3.1.7 on 2021-04-07 18:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210407_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]