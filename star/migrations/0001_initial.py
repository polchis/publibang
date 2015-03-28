# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(help_text=b'Ingrese nombre.', max_length=250, verbose_name=b'Nombre')),
                ('inicio', models.DateTimeField(help_text=b'Ingrese fecha de inicio.', verbose_name=b'Fecha de inicio')),
                ('fin', models.DateTimeField(help_text=b'Ingrese fecha de fin.', verbose_name=b'Fecha de fin')),
                ('premiacion', models.DateTimeField(help_text=b'Ingrese fecha de premiacion.', verbose_name=b'Fecha de premiacion')),
                ('estado', models.BooleanField(default=False, help_text=b'Check si esta activo.', verbose_name=b'Estado')),
            ],
            options={
                'verbose_name': 'Consurso',
                'verbose_name_plural': 'Consursos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creacion', models.DateTimeField(help_text=b'Ingrese la Fecha de Ingreso.', verbose_name=b'Fecha de Ingreso.', auto_now_add=True)),
                ('modicado', models.DateTimeField(help_text=b'Ingrese la Fecha de Modificaci\xc3\xb3n.', verbose_name=b'Fecha de Modificaci\xc3\xb3n.', auto_now=True)),
                ('concurso', models.ForeignKey(verbose_name=b'Concurso', to='star.Concurso')),
                ('usuario', models.ForeignKey(verbose_name=b'Usuario', to='security.Usuario')),
            ],
            options={
                'verbose_name': 'Participa',
                'verbose_name_plural': 'Participantes',
            },
            bases=(models.Model,),
        ),
    ]
