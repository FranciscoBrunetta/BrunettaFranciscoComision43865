# Generated by Django 4.2.4 on 2023-08-14 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cervezas',
            new_name='Cerveza',
        ),
        migrations.RenameModel(
            old_name='Espumantes',
            new_name='Espumante',
        ),
        migrations.RenameModel(
            old_name='Spirits',
            new_name='Spirit',
        ),
        migrations.RenameModel(
            old_name='Vinos',
            new_name='Vino',
        ),
        migrations.RenameModel(
            old_name='Whiskies',
            new_name='Whisky',
        ),
    ]
