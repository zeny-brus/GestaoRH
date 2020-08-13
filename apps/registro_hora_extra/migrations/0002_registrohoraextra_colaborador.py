# Generated by Django 2.2.15 on 2020-08-13 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0002_auto_20200813_1549'),
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='colaborador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='colaboradores.Colaborador'),
            preserve_default=False,
        ),
    ]
