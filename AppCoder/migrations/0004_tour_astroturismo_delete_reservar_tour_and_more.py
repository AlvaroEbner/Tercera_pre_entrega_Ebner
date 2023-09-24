# Generated by Django 4.2.5 on 2023-09-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_delete_entregable_delete_estudiante_delete_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_Astroturismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('total_adultos', models.IntegerField()),
                ('total_ninios', models.IntegerField()),
                ('fecha_tour', models.DateField()),
                ('tipo_tour', models.CharField(choices=[('observación', 'Observación'), ('astrofotografia', 'Astrofotografía')], max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Reservar_tour',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=60),
        ),
    ]