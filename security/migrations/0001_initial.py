# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frase', models.CharField(default=b'', help_text=b'Enter frase.', max_length=20, verbose_name=b'Frase')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dni', models.CharField(help_text=b'Enter dni.', max_length=250, verbose_name=b'Address')),
                ('phone', models.CharField(default=b'', help_text=b'Enter phone.', max_length=250, verbose_name=b'Phone')),
                ('operador', models.CharField(default=b'', help_text=b'Enter operador.', max_length=250, verbose_name=b'Phone')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='usuario',
            field=models.ForeignKey(verbose_name=b'Usuario', to='security.Usuario'),
        ),
    ]
