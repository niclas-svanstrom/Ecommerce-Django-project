# Generated by Django 4.2 on 2023-04-06 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename__django_db_models_fields_integerfield__product__django_db_models_fields_autofield__and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='<django.db.models.fields.AutoField>',
            new_name='image',
        ),
    ]
