# Generated by Django 5.0.6 on 2024-06-03 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario_is_estudiante_usuario_is_profesor_estudiante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=123.0, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='IngresoDatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingresos', to='core.estudiante')),
            ],
        ),
    ]
