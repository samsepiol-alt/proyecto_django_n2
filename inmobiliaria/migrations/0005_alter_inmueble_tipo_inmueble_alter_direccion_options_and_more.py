# Generated by Django 5.1.3 on 2024-12-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0004_alter_perfil_tipo_usuario_delete_tipousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='tipo_inmueble',
            field=models.CharField(choices=[('house', 'Casa'), ('department', 'Departamento'), ('plot', 'Parcela')], default='Casa', max_length=20),
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tipo_usuario',
            field=models.CharField(choices=[('landlord', 'Arrendador'), ('tenant', 'Arrendatario')], default='arrendatario', max_length=10),
        ),
        migrations.DeleteModel(
            name='InmuebleTipo',
        ),
    ]
