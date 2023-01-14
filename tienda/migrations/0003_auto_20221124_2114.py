# Generated by Django 3.2 on 2022-11-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_libro_tapa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.CharField(choices=[('cronica', 'cronica'), ('ensayo', 'ensayo'), ('narrativa', 'narrativa'), ('poesia', 'poesia')], max_length=10),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]