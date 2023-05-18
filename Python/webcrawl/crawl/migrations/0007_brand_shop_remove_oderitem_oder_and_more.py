# Generated by Django 4.2.1 on 2023-05-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0006_product_current_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_seller', models.CharField(max_length=200, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='oderitem',
            name='oder',
        ),
        migrations.RemoveField(
            model_name='oderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='oder',
        ),
        migrations.DeleteModel(
            name='Oder',
        ),
        migrations.DeleteModel(
            name='OderItem',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]