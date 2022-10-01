# Generated by Django 4.1 on 2022-09-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionIPS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamiento',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='condicion',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='empleados',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='entidad_salud',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='oficio',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='agendamiento',
            name='idAgendamiento',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='condicion',
            name='idCondicion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='idEmpleados',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='entidad_salud',
            name='idEntidad_salud',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='oficio',
            name='idOficio',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='idTransaccion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='id_Usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
