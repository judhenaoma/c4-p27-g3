# Generated by Django 3.2.8 on 2021-10-18 00:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0005_alter_inmueble_fechacreacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='fechacreacion',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 0, 30, 16, 53577, tzinfo=utc)),
        ),
    ]
