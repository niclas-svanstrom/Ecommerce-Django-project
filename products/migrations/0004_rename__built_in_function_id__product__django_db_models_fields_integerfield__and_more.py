# Generated by Django 4.2 on 2023-04-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_image_product__built_in_function_id_'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='<built-in function id>',
            new_name='<django.db.models.fields.IntegerField>',
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]