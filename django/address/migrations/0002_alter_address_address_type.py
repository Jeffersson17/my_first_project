# Generated by Django 5.1.2 on 2024-10-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('RU', 'Rua'), ('AV', 'Avenida'), ('ES', 'Estrada'), ('RO', 'Rodovia'), ('VE', 'Via expressa'), ('BE', 'Beco')], max_length=2),
        ),
    ]
