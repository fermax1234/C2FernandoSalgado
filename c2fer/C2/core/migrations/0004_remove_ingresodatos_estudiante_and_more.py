# Generated by Django 5.0.6 on 2024-06-03 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_usuario_is_active_usuario_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresodatos',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='IngresoDatos',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]