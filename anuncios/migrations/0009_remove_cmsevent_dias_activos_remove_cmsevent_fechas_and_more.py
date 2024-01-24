# Generated by Django 5.0 on 2024-01-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0008_dia_fecha_horario_remove_cmsevent_fecha_final_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmsevent',
            name='dias_activos',
        ),
        migrations.RemoveField(
            model_name='cmsevent',
            name='fechas',
        ),
        migrations.RemoveField(
            model_name='cmsevent',
            name='horarios',
        ),
        migrations.DeleteModel(
            name='Dia',
        ),
        migrations.AddField(
            model_name='cmsevent',
            name='dias_activos',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Fecha',
        ),
        migrations.AddField(
            model_name='cmsevent',
            name='fechas',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
        migrations.AddField(
            model_name='cmsevent',
            name='horarios',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
