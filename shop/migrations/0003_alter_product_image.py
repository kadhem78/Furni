# Generated by Django 5.0.6 on 2024-06-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products\\%Y\\%m\\%d'),
        ),
    ]
