# Generated by Django 4.0 on 2021-12-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zipynuts', '0005_alter_produto_peso_em_gramas_alter_produto_preço'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data_de_fabricação',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='produto',
            name='data_de_validade',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='produto',
            name='peso_em_gramas',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preço',
            field=models.CharField(max_length=20),
        ),
    ]
