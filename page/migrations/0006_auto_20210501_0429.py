# Generated by Django 2.1 on 2021-05-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_page_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='stream',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='stream',
            name='stream',
            field=models.CharField(max_length=255),
        ),
    ]
