# Generated by Django 4.0.4 on 2022-05-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
