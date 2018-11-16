# Generated by Django 2.1 on 2018-11-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('CodigoMascota', models.AutoField(primary_key=True, serialize=False)),
                ('NombreMascota', models.CharField(max_length=20)),
                ('RazaMascota', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(blank=True, null=True)),
                ('EstadoMascota', models.CharField(default=True, max_length=50)),
            ],
        ),
    ]