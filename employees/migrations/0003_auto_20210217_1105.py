# Generated by Django 3.1.6 on 2021-02-17 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20210217_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='employees.employee'),
        ),
    ]
