# Generated by Django 5.1.1 on 2024-09-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_status_product_pub_status_product_brand_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='counted_views',
            field=models.IntegerField(default=0),
        ),
    ]
