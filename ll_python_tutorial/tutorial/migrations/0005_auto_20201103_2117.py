# Generated by Django 3.1.2 on 2020-11-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0004_auto_20201024_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
    ]
