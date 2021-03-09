# Generated by Django 3.1.5 on 2021-03-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operacao',
            old_name='qtd',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='operacao',
            name='price',
        ),
        migrations.AddField(
            model_name='operacao',
            name='purchase_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='operacao',
            name='shareName',
            field=models.CharField(default='EMPRESA', max_length=10),
        ),
        migrations.AddField(
            model_name='operacao',
            name='totalOperationValue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='operacao',
            name='trading_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='operacao',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='operacao',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='operacao',
            name='type_operation',
            field=models.CharField(default='N', max_length=2),
        ),
    ]
