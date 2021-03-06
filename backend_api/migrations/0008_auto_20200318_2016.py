# Generated by Django 3.0.4 on 2020-03-18 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_auto_20200318_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leader', to='backend_api.Employee'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='backend_api.Employee'),
        ),
        migrations.DeleteModel(
            name='TeamLeader',
        ),
    ]
