# Generated by Django 4.1.7 on 2023-05-08 19:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0005_veiculo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name": "acessório", "verbose_name_plural": "acessórios"},
        ),
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "cor", "verbose_name_plural": "cores"},
        ),
        migrations.AlterModelOptions(
            name="veiculo",
            options={"verbose_name": "veículo", "verbose_name_plural": "veículos"},
        ),
    ]