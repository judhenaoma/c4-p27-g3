# Generated by Django 3.2.8 on 2021-10-14 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0006_inmueble_registroinmueble'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmueble',
            name='imagenes',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='fechacreacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='imagenes1',
            field=models.ImageField(null=True, upload_to='inmuebles/'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='imagenes2',
            field=models.ImageField(null=True, upload_to='inmuebles/'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='imagenes3',
            field=models.ImageField(null=True, upload_to='inmuebles/'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='imagenesPrincipal',
            field=models.ImageField(null=True, upload_to='inmuebles/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_houseHolder',
            field=models.BooleanField(default=True),
        ),
    ]
