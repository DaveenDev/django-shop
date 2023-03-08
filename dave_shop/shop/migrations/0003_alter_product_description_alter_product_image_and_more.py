# Generated by Django 4.1.7 on 2023-03-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_options_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product-images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]