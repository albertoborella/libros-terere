# Generated by Django 3.2 on 2022-12-20 23:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20221124_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]