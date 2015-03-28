# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frase', models.CharField(default=b'', help_text=b'Enter frase.', max_length=20, verbose_name=b'Frase')),
                ('usuario', models.ForeignKey(verbose_name=b'Usuario', to='security.Usuario')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
            bases=(models.Model,),
        ),
    ]
