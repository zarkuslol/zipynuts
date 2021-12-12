# Generated by Django 4.0 on 2021-12-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.FloatField()),
                ('peso_em_gramas', models.FloatField()),
                ('data_fabricacao', models.CharField(max_length=10)),
                ('data_validade', models.CharField(max_length=10)),
            ],
        ),
    ]
