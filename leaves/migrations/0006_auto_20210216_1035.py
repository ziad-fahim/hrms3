# Generated by Django 3.1.6 on 2021-02-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0005_remove_all_leaves_number_of_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_master',
            name='leave_type',
            field=models.CharField(max_length=50),
        ),
    ]
