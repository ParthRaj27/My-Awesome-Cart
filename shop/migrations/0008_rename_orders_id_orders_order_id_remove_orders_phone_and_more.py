# Generated by Django 4.2.2 on 2023-08-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_item_json_orders_items_json'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Orders_id',
            new_name='order_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='adress',
        ),
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
