# Generated by Django 3.0 on 2022-06-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20220604_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oppurtunities',
            name='genre',
            field=models.CharField(choices=[('O', 'ONLINE COURSE'), ('I', 'INTERNSHIP'), ('J', 'JOB')], max_length=2),
        ),
    ]
