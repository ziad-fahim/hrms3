# Generated by Django 3.1.6 on 2021-02-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20210218_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
