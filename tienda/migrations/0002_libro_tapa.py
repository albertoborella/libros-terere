# Generated by Django 3.2 on 2022-11-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='tapa',
            field=models.ImageField(blank=True, null=True, upload_to='tapas/'),
        ),
    ]
