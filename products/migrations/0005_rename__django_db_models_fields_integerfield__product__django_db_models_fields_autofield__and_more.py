# Generated by Django 4.2 on 2023-04-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename__built_in_function_id__product__django_db_models_fields_integerfield__and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='<django.db.models.fields.IntegerField>',
            new_name='<django.db.models.fields.AutoField>',
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
