# Generated by Django 4.1.7 on 2023-03-11 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_orderitems_options_alter_orderitems_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='order',
            field=models.ManyToManyField(to='shop.order'),
        ),
    ]