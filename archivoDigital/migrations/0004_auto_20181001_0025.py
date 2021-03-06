# Generated by Django 2.0.5 on 2018-10-01 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archivoDigital', '0003_auto_20180928_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivoDigital.Area', verbose_name='Área'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cargo',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='user',
            name='extension',
            field=models.IntegerField(default=1, verbose_name='Extensión'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Administrador'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Apellidos(s)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=1, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='fotoUsuarios', verbose_name='Foto de perfil'),
        ),
    ]
