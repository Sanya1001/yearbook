# Generated by Django 2.1 on 2021-04-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20210429_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(default='Science', max_length=255)),
            ],
        ),
    ]
