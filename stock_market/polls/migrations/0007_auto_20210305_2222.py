# Generated by Django 3.1.5 on 2021-03-06 01:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_auto_20210305_2119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Investor',
        ),
    ]
