# Generated by Django 3.1.5 on 2021-03-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210305_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacao',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
