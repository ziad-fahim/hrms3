# Generated by Django 3.1.6 on 2021-03-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0009_auto_20210222_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField()),
                ('start_range', models.IntegerField()),
                ('end_range', models.IntegerField(null=True)),
                ('difference', models.IntegerField(null=True)),
                ('tax', models.IntegerField(null=True)),
            ],
        ),
    ]
