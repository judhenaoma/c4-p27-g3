# Generated by Django 3.2.8 on 2021-10-17 23:38

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0003_auto_20211017_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='id_url',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='titulo', unique=True),
        ),
    ]
