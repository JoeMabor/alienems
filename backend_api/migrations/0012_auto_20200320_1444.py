# Generated by Django 3.0.4 on 2020-03-20 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0011_auto_20200320_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='work_arrangement',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='backend_api.WorkArrangement'),
            preserve_default=False,
        ),
    ]
