# Generated by Django 3.1.2 on 2020-10-21 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_chapter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='display_name',
            new_name='displayName',
        ),
    ]
