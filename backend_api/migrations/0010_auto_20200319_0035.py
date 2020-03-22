# Generated by Django 3.0.4 on 2020-03-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0009_auto_20200319_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamleader',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamLeader', to='backend_api.Employee'),
        ),
    ]