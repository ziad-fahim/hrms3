# Generated by Django 3.1.6 on 2021-02-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0006_auto_20210216_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_leaves',
            name='Status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Waiting to approve', 'Waiting to approve')], default='WAITING FOR APPROVE', max_length=20),
        ),
    ]
