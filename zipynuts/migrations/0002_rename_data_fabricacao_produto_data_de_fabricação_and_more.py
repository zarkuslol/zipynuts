# Generated by Django 4.0 on 2021-12-12 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zipynuts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='data_fabricacao',
            new_name='data_de_fabricação',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='data_validade',
            new_name='data_de_validade',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='preco',
            new_name='preço',
        ),
    ]
