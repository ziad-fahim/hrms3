# Generated by Django 3.1.6 on 2021-02-22 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20210218_1454'),
        ('leaves', '0008_auto_20210218_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_leaves',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp', to='employees.employee'),
        ),
    ]
