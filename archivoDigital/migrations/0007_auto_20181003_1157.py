# Generated by Django 2.0.5 on 2018-10-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivoDigital', '0006_auto_20181001_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='changePass',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Cambio de password'),
        ),
    ]